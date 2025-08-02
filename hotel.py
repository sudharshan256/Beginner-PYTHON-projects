import datetime

class HotelManagementSystem:
    def __init__(self):
        # Rooms data: room_number -> {type, price, is_booked}
        self.rooms = {
            101: {"type": "Single", "price": 1000, "is_booked": False},
            102: {"type": "Double", "price": 1800, "is_booked": False},
            201: {"type": "Suite", "price": 3000, "is_booked": False}
        }
        # Bookings: booking_id -> booking details
        self.bookings = {}
        self.next_booking_id = 1

    def show_rooms(self):
        print("Available Rooms:")
        for rn, info in self.rooms.items():
            status = "Booked" if info["is_booked"] else "Available"
            print(f"Room {rn}: {info['type']} - ₹{info['price']} - {status}")

    def book_room(self, room_number, guest_name, check_in_str, check_out_str):
        if room_number not in self.rooms:
            print("Room does not exist.")
            return
        if self.rooms[room_number]["is_booked"]:
            print("Room is already booked.")
            return

        try:
            check_in = datetime.datetime.strptime(check_in_str, "%d/%m/%Y")
            check_out = datetime.datetime.strptime(check_out_str, "%d/%m/%Y")
            if check_out <= check_in:
                print("Check-out date must be after check-in date.")
                return
        except ValueError:
            print("Invalid date format. Use DD/MM/YYYY.")
            return

        booking_id = self.next_booking_id
        self.next_booking_id += 1

        self.bookings[booking_id] = {
            "room_number": room_number,
            "guest_name": guest_name,
            "check_in": check_in,
            "check_out": check_out
        }
        self.rooms[room_number]["is_booked"] = True

        print(f"Booking successful! Your booking ID is {booking_id}.")

    def cancel_booking(self, booking_id):
        if booking_id not in self.bookings:
            print("Booking ID not found.")
            return
        room_number = self.bookings[booking_id]["room_number"]
        self.rooms[room_number]["is_booked"] = False
        del self.bookings[booking_id]
        print(f"Booking {booking_id} cancelled successfully.")

    def show_bookings(self):
        if not self.bookings:
            print("No current bookings.")
            return
        print("Current Bookings:")
        for bid, details in self.bookings.items():
            ci = details["check_in"].strftime("%d/%m/%Y")
            co = details["check_out"].strftime("%d/%m/%Y")
            print(f"Booking ID: {bid} | Guest: {details['guest_name']} | Room: {details['room_number']} | Check-in: {ci} | Check-out: {co}")

def main():
    system = HotelManagementSystem()
    while True:
        print("\nHotel Booking Management System")
        print("1. Show Rooms")
        print("2. Book Room")
        print("3. Cancel Booking")
        print("4. Show Bookings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            system.show_rooms()
        elif choice == '2':
            guest_name = input("Enter guest name: ")
            room_number = int(input("Enter room number to book: "))
            check_in = input("Enter check-in date (DD/MM/YYYY): ")
            check_out = input("Enter check-out date (DD/MM/YYYY): ")
            system.book_room(room_number, guest_name, check_in, check_out)
        elif choice == '3':
            booking_id = int(input("Enter booking ID to cancel: "))
            system.cancel_booking(booking_id)
        elif choice == '4':
            system.show_bookings()
        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
