import random

# Generate OTP
def generateOTP():
    # Define a string of all possible characters for the OTP
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    OTP = ""

    # Loop to generate random characters and append them to OTP
    for i in range(6):
        OTP += chars[random.randint(0, len(chars)-1)]

    return OTP

# Send OTP to user's mobile/email
def sendOTP(mobile_no, email_id, OTP):
    # Code to send OTP via SMS or email
    print("OTP sent successfully")

# Verify OTP entered by user
def verifyOTP(OTP, user_input):
    if OTP == user_input:
        print("OTP verified successfully")
    else:
        print("Incorrect OTP, please try again")

# Main function to generate and verify OTP
def main():
    mobile_no = input("Enter your mobile number: ")
    email_id = input("Enter your email ID: ")

    OTP = generateOTP()

    sendOTP(mobile_no, email_id, OTP)

    user_input = input("Enter the OTP received: ")

    verifyOTP(OTP, user_input)

if __name__ == "__main__":
    main()