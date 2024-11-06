import streamlit as st
import time

# App Title
st.title("🚆 Train Management System")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = ["Train", "Ticket", "Passenger", "Station", "Platform", "Employee", "Book Ticket", "Cancel Ticket", "Notifications", "Stops At", "Managed By"]
selection = st.sidebar.selectbox("Choose section", options)

# Add balloons as a welcome animation
st.balloons()

# Helper function for simulated saving/loading with spinner animation
def simulate_processing():
    with st.spinner("Processing..."):
        time.sleep(1)

# Forms and Fields for each section
if selection == "Train":
    st.header("🚄 Train Information")
    train_id = st.text_input("Train ID")
    train_name = st.text_input("Train Name")
    train_type = st.selectbox("Type", ["Express", "Local", "Intercity"])
    max_capacity = st.number_input("Max Capacity", min_value=1)
    if st.button("Save Train Details"):
        simulate_processing()
        st.success("Train details saved successfully!")
        st.balloons()

elif selection == "Ticket":
    st.header("🎟️ Ticket Information")
    ticket_id = st.text_input("Ticket ID")
    passenger_id = st.text_input("Passenger ID")
    train_id = st.text_input("Train ID")
    seat_number = st.text_input("Seat Number")
    ticket_status = st.selectbox("Ticket Status", ["Booked", "Cancelled"])
    if st.button("Save Ticket Information"):
        simulate_processing()
        st.success("Ticket information saved successfully!")

elif selection == "Passenger":
    st.header("🧍 Passenger Details")
    passenger_id = st.text_input("Passenger ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    contact_info = st.text_input("Contact Information")
    if st.button("Save Passenger Details"):
        simulate_processing()
        st.success("Passenger details saved successfully!")

elif selection == "Station":
    st.header("🚉 Station Information")
    station_id = st.text_input("Station ID")
    station_name = st.text_input("Station Name")
    location = st.text_input("Location")
    if st.button("Save Station Information"):
        simulate_processing()
        st.success("Station information saved successfully!")

elif selection == "Platform":
    st.header("🛤️ Platform Management")
    platform_id = st.text_input("Platform ID")
    station_id = st.text_input("Station ID")
    platform_number = st.number_input("Platform Number", min_value=1)
    if st.button("Save Platform Details"):
        simulate_processing()
        st.success("Platform details saved successfully!")

elif selection == "Employee":
    st.header("👷 Employee Details")
    employee_id = st.text_input("Employee ID")
    name = st.text_input("Employee Name")
    role = st.text_input("Role")
    contact_info = st.text_input("Contact Information")
    if st.button("Save Employee Details"):
        simulate_processing()
        st.success("Employee details saved successfully!")

elif selection == "Book Ticket":
    st.header("📝 Book Ticket")
    passenger_id = st.text_input("Passenger ID")
    train_id = st.text_input("Train ID")
    station_from = st.text_input("From Station ID")
    station_to = st.text_input("To Station ID")
    travel_date = st.date_input("Travel Date")
    seat_preference = st.selectbox("Seat Preference", ["Window", "Aisle", "Any"])
    if st.button("Book Ticket"):
        simulate_processing()
        st.success("Ticket booked successfully!")
        st.balloons()

elif selection == "Cancel Ticket":
    st.header("❌ Cancel Ticket")
    ticket_id = st.text_input("Ticket ID")
    cancellation_reason = st.text_area("Reason for Cancellation")
    if st.button("Cancel Ticket"):
        simulate_processing()
        st.success("Ticket canceled successfully!")

elif selection == "Notifications":
    st.header("🔔 Send Notifications")
    notification_id = st.text_input("Notification ID")
    message = st.text_area("Notification Message")
    recipient_type = st.selectbox("Send To", ["All Passengers", "Employees", "Specific Train"])
    if st.button("Send Notification"):
        simulate_processing()
        st.success("Notification sent successfully!")

elif selection == "Stops At":
    st.header("🛑 Manage Train Stops")
    train_id = st.text_input("Train ID")
    station_id = st.text_input("Station ID")
    arrival_time = st.time_input("Arrival Time")
    departure_time = st.time_input("Departure Time")
    if st.button("Add Stop"):
        simulate_processing()
        st.success("Stop added successfully!")

elif selection == "Managed By":
    st.header("👨‍✈️ Manage Train Managers")
    train_id = st.text_input("Train ID")
    employee_id = st.text_input("Employee ID")
    role = st.text_input("Role (e.g., Conductor, Engineer)")
    if st.button("Assign Manager"):
        simulate_processing()
        st.success("Manager assigned successfully!")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Train Management System created with Streamlit.")
