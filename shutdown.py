def shutdown():
    print("Starting shutdown...")
    terminate_processes = input("Do you want to terminate all processes and ongoing applications? (yes/no) ").lower()
    if terminate_processes == "yes":
        print("Closing apps and processes...")
    elif terminate_processes == "no":
        print("Shutdown cannot continue unless you close all processes and ongoing applications. Aborting shutdown.")
        return
    else:
        print("Sorry, you entered an invalid answer. Please try again.")
        return
    shutdown_allUsers = input("Other people may be using the system. Continuing will shut down their accounts/computers as well. Do you wish to continue? (yes/no) ").lower()
    if shutdown_allUsers == "yes":
        print("Shutting down all accounts/computers on the system...")
    elif shutdown_allUsers == "no":
        print("Shutdown cannot continue unless you shut down all accounts/computers on the system. Aborting shutdown.")
        return
    else:
        print("Sorry, you entered an invalid answer. Please try again.")
        return
    update_onLaunch = input("Would you like to update your OS to the latest version (if applicable) when you turn on your PC? (yes/no) ").lower()
    if update_onLaunch == "yes":
        print("Your OS will update the next time you turn on your PC.")
    elif update_onLaunch == "no":
        print("Your OS will not update automatically the next time you start your PC. You can still update it manually from Settings.")
    else:
        print("Sorry, you entered an invalid answer. Please try again.")
        return
    print("Proceeding to shutdown...")
    print("Goodbye.")

shutdown()