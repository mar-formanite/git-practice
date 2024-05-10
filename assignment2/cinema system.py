class Movies:
    def __init__(self, title, available_seats, selected_seats):
        self.title = title
        self.available_seats = available_seats
        self.selected_seats = selected_seats
        self.bookings = []
    def record_booking(self):
        self.bookings.extend(self.selected_seats)
        self.available_seats -= len(self.selected_seats)
        booking_details = BookingDetails("123456", self.selected_seats, "2024-05-20", self.title)
        BookingDetails.save_booking_details(booking_details)
    def __str__(self):
        return f"Movies title:{self.title},Available seats:{self.available_seats}"
class TimeSlot:
    def __init__(self, t_starting, t_ending, screening_date):
        self.start_time = t_starting
        self.end_time = t_ending
        self.screening_date = screening_date
    def __str__(self):
        return f"Starting time:{self.start_time},Ending time:{self.end_time},Screening date:{self.screening_date}"
class CinemaScreen:
    def __init__(self, screen_number):
        self.screen_number = screen_number
    def __str__(self):
        screen_list = []
        for i in range(1, self.screen_number + 1):
            screen_list.append(f"Screen Number : {i}")
        return screen_list
class BookingDetails:
    def __init__(self, booking_id, selected_seats, screening_date, movie_details):
        self.booking_id = booking_id
        self.movie_details = movie_details
        self.selected_seats = selected_seats
        self.screening_date = screening_date
    def __str__(self):
        return f"Booking ID:{self.booking_id}, Movie Details:{self.movie_details},Selected Seats: {','.join(self.selected_seats)}, Screening Date: {self.screening_date}"
    @staticmethod
    def save_booking_details(booking_details):
        try:
            with open("booking_details.txt", "a") as file:
                file.write(str(booking_details) + '\n')
            print("Booking details saved successfully.")
        except Exception as e:
            print(f"Error occurred while saving booking details: {e}")
class User:
    def __init__(self, username):
        self.username = username
        self.logged_in = False
        self.select_movie = None
    def register(self):
        print("WELCOME TO CINEMA BOOKING SYSTEM!")
        print("Please register to get access!")
        self.username = input("Enter the username you like:")
        print(f"User {self.username} has been registered.")
        self.logged_in = True
    def login(self):
        print("Login to your account!")
        if self.logged_in:
            print(f"User {self.username} has logged in.")
        else:
            input_username = input("Enter your username:")
            if input_username == self.username:
                print(f"User {self.username} has logged in.")
                self.logged_in = True
            else:
                print("Invalid username. Please register or try again.")

    def browse_movies(self):
        try:
            with open("movie_listings.txt", "r") as file:
                movie_listing = file.readlines()
                print("Movie Listings:")
            for i, movie in enumerate(movie_listing, 1):
                print(f"{i}. {movie.strip()}")
            selection = int(input("Enter the number of the movie you want to select: "))
            if 1 <= selection <= len(movie_listing):
                selected_movie = movie_listing[selection - 1].strip()
                print(f"You selected: {selected_movie}")
                self.select_movie = Movies(selected_movie, 100, [])
            else:
                print("Invalid selection. Please try again.")
        except FileNotFoundError:
            print("Movie listings file not found.")
        except ValueError:
                for index, movie in movie_index_mapping.items():
                    if user_input.lower() in movie.lower():
                        self.select_movie = movie
                        print(f"You have selected the movie: {self.select_movie}")
                        break
                else:
                    print("Movie not found. Please try again.")
    def chosen_seats(self):
        if self.select_movie:
            print(f"Available seats for {self.select_movie['title']}: {self.select_movie['available_seats']}")
            seats_input = input("Enter seats separated by commas (e.g., A1, A2): ")
            self.selected_seats = seats_input.strip().split(",")
            print(f"Selected seats: {', '.join(self.selected_seats)}")
        else:
            print("No movie selected.")
    def reserve_seats(self):
        if self.select_movie and self.selected_seats:
            booking_details = BookingDetails("123456", self.selected_seats, "2024-05-20", self.select_movie)
            print("Booking details:")
            print(booking_details)
            BookingDetails.save_booking_details(booking_details)
        else:
            print("No movie selected or seats chosen.")
class SystemAdministrator:
    MOVIE_LISTINGS_FILE = "movie_listings.txt"
    @staticmethod
    def configure_system(movie_listings, screens):
        try:
            with open(SystemAdministrator.MOVIE_LISTINGS_FILE, "w") as file:
                for movie in movie_listings:
                    file.write(movie['title'] + '\n')
            print("System configuration saved successfully.")
        except Exception as e:
            print(f"Error occurred while saving system configuration:{e} ")
    @staticmethod
    def display_movie_listings():
        try:
            with open("movie_listings.txt", "r") as file:
                movie_listings = file.readlines()
                print("Movie Listings:")
                for movie in movie_listings:
                    print(movie.strip())
        except FileNotFoundError:
            print("Movie listings file not found.")
    @staticmethod
    def display_screens():
        try:
            with open("screens.txt", "r") as file:
                screens = file.readlines()
                print("Screens:")
                for screen_number, screen_details in enumerate(screens, 1):
                    print(f"Screen Number : {screen_number}, Details: {screen_details.strip()}")
        except FileNotFoundError:
            print("Screens file not found.")
    @staticmethod
    def load_booking_details():
        try:
            with open("booking_details.txt", "r") as file:
                booking_details = file.readlines()
                print("Booking Details:")
                for booking in booking_details:
                    print(booking.strip())
        except FileNotFoundError:
            print("Booking details file not found.")
    @staticmethod
    def save_state(filename, obj):
        try:
            with open(filename, "w") as file:
                file.write(str(obj))
            print("Object saved successfully.")
        except Exception as e:
            print(f"Error occurred while saving object: {e}")
    @staticmethod
    def load_state(filename):
        try:
            with open(filename, "r") as file:
                obj = file.read()
                print("Object loaded successfully.")
                return obj
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error occurred while loading object: {e}")
def main():
    username = input("Enter your username: ")
    user_type = input("Are you an admin or a regular user? (admin/user): ").lower()
    if user_type == "admin":
        user = SystemAdministrator()
        user_type = "admin"
    elif user_type == "user":
        user = User(username)
        user_type = "user"
    else:
        print("Invalid user type. Please enter 'admin' or 'user'.")
        return
    if user_type == "user":
        user.register()
        user.login()
        user.browse_movies()
        user.chosen_seats()
        user.reserve_seats()
    if user_type == "admin":
        SystemAdministrator.display_movie_listings()
        SystemAdministrator.display_screens()
        SystemAdministrator.load_booking_details()
        SystemAdministrator.save_state("system_state.txt", {"example_data": "example_value"})
        SystemAdministrator.load_state("system_state.txt")
if __name__ == "__main__":
    main()
