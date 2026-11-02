def vacuum_cleaner(room_count):
    rooms = {}
    for index in range(room_count):
        name = input("Enter name of room " + str(index + 1) + ": ").strip()
        status = input("Is " + name + " dirty? (yes/no): ").strip().lower()
        rooms[name] = status == "yes"

    current = input("Enter starting room: ").strip()
    if current not in rooms:
        print("Starting room does not exist.")
        return

    order = list(rooms)
    start_index = order.index(current)
    visit_order = order[start_index:] + order[:start_index]
    for room in visit_order:
        print("Vacuum cleaner is in", room)
        if rooms[room]:
            print("Cleaning", room)
            rooms[room] = False
        else:
            print(room, "is already clean")
    print("All rooms are clean.")


room_count = int(input("Enter number of rooms: "))
if room_count <= 0:
    print("The number of rooms must be positive.")
else:
    vacuum_cleaner(room_count)
