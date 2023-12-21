from function import enter, show_available_places, register_place, unregister_place, show_registered_places

while True:
    print("exit | enter [0|1]")
    option = int(input("option: "))
    current_user = None
    if option == 0:
        break
    elif option == 1:
        current_user = enter()

    while current_user:
        print("back | see available places | see registered places[0|1|2]")
        option = int(input("option: "))
        if option == 0:
            break
        elif option == 1:
            show_available_places()

            while True:
                print("back | register | unregister [0|1|2]")
                option = int(input("option: "))
                if option == 0:
                    break
                elif option == 1:
                    register_place(current_user)
                elif option == 2:
                    unregister_place(current_user)
        elif option == 2:
            show_registered_places(current_user)
