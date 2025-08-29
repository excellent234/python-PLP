# Assignment 1: Design Your Own Class! 🏗️

class ElectronicDevice:
    """
    A base class representing a generic electronic device.
    Demonstrates basic attributes and a common method.
    """
    def __init__(self, brand, model, power_status="off"):
        """
        Constructor to initialize an ElectronicDevice object.

        Args:
            brand (str): The brand of the device.
            model (str): The model name of the device.
            power_status (str): The current power status ('on' or 'off').
        """
        self.brand = brand
        self.model = model
        self.power_status = power_status
        print(f"Created a new Electronic Device: {self.brand} {self.model}")

    def turn_on(self):
        """Turns the device on."""
        if self.power_status == "off":
            self.power_status = "on"
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def turn_off(self):
        """Turns the device off."""
        if self.power_status == "on":
            self.power_status = "off"
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def display_info(self):
        """Prints basic information about the device."""
        print(f"--- Device Info ---")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  Power: {self.power_status.upper()}")
        print(f"-------------------")


class Smartphone(ElectronicDevice):
    """
    A specialized class representing a Smartphone, inheriting from ElectronicDevice.
    Adds specific attributes and methods for a smartphone.
    """
    def __init__(self, brand, model, storage_gb, price, os_version, power_status="off"):
        """
        Constructor for a Smartphone, calling the parent class constructor
        and adding smartphone-specific attributes.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model name of the smartphone.
            storage_gb (int): The internal storage in Gigabytes.
            price (float): The price of the smartphone.
            os_version (str): The operating system version.
            power_status (str): The current power status ('on' or 'off').
        """
        super().__init__(brand, model, power_status) # Initialize parent class
        self.storage_gb = storage_gb
        self.price = price
        self.os_version = os_version
        self.apps_installed = []
        print(f"  -> Specifically, a Smartphone with {self.storage_gb}GB storage.")

    def make_call(self, number):
        """Simulates making a call if the phone is on."""
        if self.power_status == "on":
            print(f"{self.brand} {self.model} is calling {number}...")
        else:
            print(f"Cannot make call. {self.brand} {self.model} is OFF.")

    def install_app(self, app_name):
        """Installs an app on the phone."""
        if self.power_status == "on":
            if app_name not in self.apps_installed:
                self.apps_installed.append(app_name)
                print(f"'{app_name}' installed on {self.model}.")
            else:
                print(f"'{app_name}' is already installed.")
        else:
            print(f"Cannot install app. {self.brand} {self.model} is OFF.")

    def display_info(self):
        """
        Overrides the display_info method from ElectronicDevice to
        include smartphone-specific details.
        This demonstrates polymorphism (same method name, different behavior).
        """
        super().display_info() # Call parent's display_info for common info
        print(f"  Storage: {self.storage_gb} GB")
        print(f"  Price: ${self.price:,.2f}")
        print(f"  OS Version: {self.os_version}")
        print(f"  Apps: {', '.join(self.apps_installed) if self.apps_installed else 'No apps'}")
        print(f"-------------------")


class AndroidSmartphone(Smartphone):
    """
    A further specialized class for Android Smartphones, inheriting from Smartphone.
    Demonstrates another layer of inheritance and potential for unique behaviors.
    """
    def __init__(self, brand, model, storage_gb, price, os_version, android_version, power_status="off"):
        """
        Constructor for an AndroidSmartphone, calling the parent Smartphone constructor
        and adding an Android-specific attribute.
        """
        super().__init__(brand, model, storage_gb, price, os_version, power_status)
        self.android_version = android_version
        print(f"  -> It's an Android Phone running {self.android_version}.")

    def open_google_play_store(self):
        """Simulates opening the Google Play Store."""
        if self.power_status == "on":
            print(f"Opening Google Play Store on {self.model} (Android {self.android_version})...")
        else:
            print(f"Cannot open Play Store. {self.brand} {self.model} is OFF.")

    def display_info(self):
        """
        Further overrides display_info to include Android-specific version.
        """
        super().display_info()
        print(f"  Android Version: {self.android_version}")
        print(f"-------------------")


print("--- Assignment 1: Design Your Own Class! 🏗️ ---")
my_phone = Smartphone("Samsung", "Galaxy S23", 256, 799.99, "Android 14")
my_phone.turn_on()
my_phone.make_call("555-123-4567")
my_phone.install_app("Instagram")
my_phone.install_app("WhatsApp")
my_phone.display_info()
my_phone.turn_off()
my_phone.make_call("555-987-6543") # Will show it's off

print("\n--- Exploring Inheritance ---")
android_device = AndroidSmartphone("Google", "Pixel 8", 128, 699.00, "Android 14", "Vanilla Android")
android_device.turn_on()
android_device.install_app("Maps")
android_device.open_google_play_store()
android_device.display_info()
android_device.turn_off()
print("-" * 30)

# Assignment 2: Polymorphism Challenge! 🎭

class Vehicle:
    """
    A base class for vehicles with a common 'move' method.
    """
    def __init__(self, name):
        self.name = name

    def move(self):
        """
        A generic move method that will be overridden by subclasses.
        """
        print(f"{self.name} is moving in a generic way.")

class Car(Vehicle):
    """
    A Car class inheriting from Vehicle, defining its own 'move' behavior.
    """
    def __init__(self, name, make):
        super().__init__(name)
        self.make = make

    def move(self):
        """
        Car-specific move action. 🚗
        """
        print(f"{self.make} {self.name} is Driving 🚗 down the road.")

class Plane(Vehicle):
    """
    A Plane class inheriting from Vehicle, defining its own 'move' behavior.
    """
    def __init__(self, name, airline):
        super().__init__(name)
        self.airline = airline

    def move(self):
        """
        Plane-specific move action. ✈️
        """
        print(f"{self.airline}'s {self.name} is Flying ✈️ through the sky!")

class Boat(Vehicle):
    """
    A Boat class inheriting from Vehicle, defining its own 'move' behavior.
    """
    def __init__(self, name, type_of_boat):
        super().__init__(name)
        self.type_of_boat = type_of_boat

    def move(self):
        """
        Boat-specific move action. ⛵
        """
        print(f"The {self.type_of_boat} {self.name} is Sailing ⛵ across the water.")

print("\n--- Assignment 2: Polymorphism Challenge! 🎭 ---")

# Create a list of different vehicle objects
vehicles = [
    Car("Civic", "Honda"),
    Plane("Boeing 747", "British Airways"),
    Car("Mustang", "Ford"),
    Boat("Sea Wanderer", "Sailboat"),
    Plane("Airbus A380", "Emirates")
]

# Iterate through the list and call the 'move' method on each vehicle.
# This demonstrates polymorphism: the same 'move()' call behaves differently
# based on the object's actual type.
for vehicle in vehicles:
    vehicle.move()

print("-" * 30)

