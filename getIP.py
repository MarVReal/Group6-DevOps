import socket
import tkinter as tk
import tkinter.simpledialog as simpledialog
import requests
from tkinter.ttk import Frame, Label, Button

class IPInfoApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()

    def initUI(self):
        self.master.title("IP Information")
        self.pack(fill="both", expand=True)

        self.public_ip_label = Label(self, text="Public IP: ")
        self.public_ip_label.pack(pady=5)

        self.private_ip_label = Label(self, text="Private IP: ")
        self.private_ip_label.pack(pady=5)

        self.location_label = Label(self, text="Location: ")
        self.location_label.pack(pady=5)

        self.update_info_button = Button(self, text="Update Info", command=self.update_info)
        self.update_info_button.pack(pady=10)

    def update_info(self):
        public_ip = self.get_public_ip()
        private_ip = self.get_private_ip()
        location_info = self.get_location(public_ip)

        self.public_ip_label.config(text=f"Public IP: {public_ip}")
        self.private_ip_label.config(text=f"Private IP: {private_ip}")
        self.location_label.config(text=f"Location: {location_info}")

    def get_public_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]

    def get_private_ip(self):
        private_ip = None
        is_admin = self.ask_admin()
        if is_admin:
            admin_password = self.ask_password()
            with open('admin_password.txt', 'r') as f:
                stored_password = f.read().strip()
            if admin_password == stored_password:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect(('8.8.8.8', 80))
                    private_ip = s.getsockname()[0]
                    s.close()
                except Exception as e:
                    print(f"Error occurred while fetching private IP: {e}")
            else:
                tk.messagebox.showerror("Error", "Incorrect administrator password")
        else:
            self.private_ip_label.config(text="Private IP: Not available for non-administrators")
        return private_ip

    def ask_admin(self):
        is_admin = tk.messagebox.askyesno("Administrator Check", "Are you the administrator?")
        return is_admin

    def ask_password(self):
        admin_password = simpledialog.askstring("Administrator Password", "Please enter the administrator password:", show='*')
        return admin_password

    def get_location(self, ip):
        response = requests.get(f'https://ipapi.co/{ip}/json/').json()
        location_data = f"City: {response.get('city')}, " \
                        f"Region: {response.get('region')}, " \
                        f"Country: {response.get('country_name')}, " \
                        f"Time Zone: {response.get('timezone')}, " \
                        f"ISP: {response.get('org')}, " \
                        f"Latitude: {response.get('latitude')}, " \
                        f"Longitude: {response.get('longitude')}"
        return location_data

def main():
    root = tk.Tk()
    app = IPInfoApp(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()