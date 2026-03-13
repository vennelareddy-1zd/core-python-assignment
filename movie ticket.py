def book_seat(seat, booked_seats):
    if seat in booked_seats:
        print("Seat already booked")
    else:
        booked_seats.append(seat)

def cancel_seat(seat, booked_seats):
    if seat in booked_seats:
        booked_seats.remove(seat)
    else:
        print("Seat was not booked")


total_seats = 10
booked_seats = [2, 5, 7]

book_seat_number = 3
cancel_seat_number = 5

book_seat(book_seat_number, booked_seats)
cancel_seat(cancel_seat_number, booked_seats)

available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

print("Available seats:", available_seats)
