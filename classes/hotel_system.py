"""
Create a hotel reservation system which books hotel rooms.
- It charges various rates for particular sections of the hotel.
Example, Hotel rooms have penthouse suites which cost more.

- system can keep track of when rooms will be available and can be scheduled.
- people can book a room.
- people can check if a certain room is available

- Admin can:
    - add new room
        each room has a type, cost, availability status
    - add update room details

- Rooms:
    - can be available or not
    - Two or more rooms can belong to one type. Types equals ,
    - All rooms have specific different prices

"""
class Hotel:
    def __init__(self, list_room = []):
        self.list_room = list_room

    def add_room(self, room):
        self.list_room.append(room)
        print('Room added successfully')
        # for show in self.list_room:
        #     print(show.type, show.price)

    def room_check(self, avail):
        for room in self.list_room:
            if room.self.list_room(avail) == True:
                print('Room {} cost {} is avaliable'.format(self.type, self.price))
            else:
                print("Room currently not available")

    def book_room(self, type=''):
        print('Which room type do you want?')
        option = input('1 for self contain \n 2 for penthouse:')
        for rm in Hotel.self.list_room:
            if rm.self.type == 'self contain':
                Rooms.room_check()
            elif rm.self.type == 'penthouse':
                pass

    def update_room(self, ):
        pass

class Rooms:
    def __init__(self, availability='', type='', price=''):
        self.availability = input('Enter status:')
        self.type = input('Enter room type:')
        self.price = input('Enter cost:')

def logic():
    while True:
        hot = Hotel()
        print('What do you want to do?')
        choice = int(input('1 to Add room \n 2 to check availability \n 3 to Book room:'))

        if choice == 1:
            room = Rooms()
            hot.add_room(room)

        elif choice == 2:
            hot.room_check()

        elif choice == 3:
            hot.book_room()

logic()