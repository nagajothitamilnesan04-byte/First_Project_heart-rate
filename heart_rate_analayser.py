print("===== HEART RATE ANALYZER =====")
heart_rate = int(input("Enter Heart Rate (beats per minute): "))
if heart_rate < 60:
    status = "LOW HEART RATE"
elif 60 <= heart_rate <= 100:
    status = "NORMAL HEART RATE"
else:
    status = "HIGH HEART RATE"
print("\n------ RESULT ------")
print("Heart Rate:", heart_rate)
print("Condition:", status)
print("----------------------")
