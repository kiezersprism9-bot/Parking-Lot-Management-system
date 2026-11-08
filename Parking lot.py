


slot = 5
income = 0
vehicles = []


while True:
    print("\n===== PARKING MANAGEMENT SYSTEM =====")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. View Parking Slots")
    print("4. Daily Income Summary")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if slot == 0:
        print("")
        print("\n===== PARKING MANAGEMENT SYSTEM =====")
        print("no slot available")
        continue

    if choice == "1":
        type = input("enter vehicle type : ")
        plate = input("Enter plate number :")
        time = int(input("enter time (24 hours format)"))
        print("")
        print(f" type : {type}, parked success fully")
        vehicles.append({
            "type": type,
            "plate": plate,
            "time_in": time
        })
        slot -= 1
    elif choice == "2":

        vehicle_type = input("Enter vehicle type: ")
        plate = input("Enter plate number: ")
        out = int(input("Enter time out: "))

        found = False

        for vehicle in vehicles:

            if vehicle["type"] == vehicle_type and vehicle["plate"] == plate:
                parked_hours = out - vehicle["time_in"]

                fee = parked_hours * 50
                income += fee

                print("\nVehicle Found!")
                print(f"Type: {vehicle['type']}")
                print(f"Plate: {vehicle['plate']}")
                print(f"Time In: {vehicle['time_in']}")
                print(f"Time Out: {out}")
                print(f"Hours Parked: {parked_hours}")
                print(f"total Fee: {fee}")

                found = True

                vehicles.remove(vehicle)
                slot += 1

                break

            elif found == False:
                print("No vehicle found.")

    elif choice == "3":
        print("")
        print("\n===== PARKING MANAGEMENT SYSTEM =====")
        print(f"Remainig slots : {slot}")

    elif choice == "4":
        print("")
        print("\n===== PARKING MANAGEMENT SYSTEM =====")
        print(f"Total income : $ {income}" )






