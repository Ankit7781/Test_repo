import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model/dt_model.pkl")

# Full State List
states = [
    'Assam', 'Andhra Pradesh', 'Karnataka', 'Kerala', 'Meghalaya', 'Tamil Nadu', 'Goa', 'Bihar', 'Chhattisgarh',
    'Gujarat', 'Haryana', 'Himachal Pradesh', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Mizoram', 'Nagaland',
    'Punjab', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'Jammu and Kashmir', 'Jharkhand', 'West Bengal',
    'Telangana', 'Arunachal Pradesh', 'Odisha', 'Delhi', 'Sikkim', 'Rajasthan'
]

# Full District List
districts = [
    'Anantapur', 'Krishna', 'West Godavari', 'Adilabad', 'Chittoor', 'East Godavari', 'Guntur', 'Kadapa',
    'Karimnagar', 'Khammam', 'Kurnool', 'Mahabubnagar', 'Medak', 'Nalgonda', 'Nizamabad', 'Prakasam', 'Rangareddi',
    'Sri Potti Sriramulu Nellore', 'Srikakulam', 'Visakhapatanam', 'Vizianagaram', 'Warangal', 'Anjaw', 'Changlang',
    'Dibang Valley', 'East Kameng', 'East Siang', 'Kurung Kumey', 'Lohit', 'Lower Dibang Valley', 'Lower Subansiri',
    'Papum Pare', 'Tawang', 'Tirap', 'Upper Siang', 'Upper Subansiri', 'West Kameng', 'West Siang', 'Baksa', 'Barpeta',
    'Bongaigaon', 'Cachar', 'Chirang', 'Darrang', 'Dhemaji', 'Dhubri', 'Dibrugarh', 'Dima Hasao', 'Goalpara', 'Golaghat',
    'Hailakandi', 'Jorhat', 'Kamrup', 'Kamrup Metro', 'Karbi Anglong', 'Karimganj', 'Kokrajhar', 'Lakhimpur', 'Marigaon',
    'Nagaon', 'Nalbari', 'Sivasagar', 'Sonitpur', 'Tinsukia', 'Udalguri', 'Araria', 'Arwal', 'Aurangabad', 'Banka',
    'Begusarai', 'Bhagalpur', 'Bhojpur', 'Buxar', 'Darbhanga', 'Gaya', 'Gopalganj', 'Jamui', 'Jehanabad', 'Kaimur (Bhabua)',
    'Katihar', 'Khagaria', 'Kishanganj', 'Lakhisarai', 'Madhepura', 'Madhubani', 'Munger', 'Muzaffarpur', 'Nalanda',
    'Nawada', 'Pashchim Champaran', 'Patna', 'Purbi Champaran', 'Purnia', 'Rohtas', 'Saharsa', 'Samastipur', 'Saran',
    'Sheikhpura', 'Sheohar', 'Sitamarhi', 'Siwan', 'Supaul', 'Vaishali', 'Bastar', 'Bijapur', 'Bilaspur',
    'Dakshin Bastar Dantewada', 'Dhamtari', 'Durg', 'Janjgir-Champa', 'Jashpur', 'Kabirdham', 'Kanker', 'Korba', 'Korea',
    'Mahasamund', 'Narayanpur', 'Raigarh', 'Raipur', 'Rajnandgaon', 'Surguja', 'North Goa', 'South Goa', 'Ahmadabad',
    'Amreli', 'Anand', 'Banas Kantha', 'Bharuch', 'Bhavnagar', 'Dang', 'Dohad', 'Gandhinagar', 'Jamnagar', 'Junagadh',
    'Kachchh', 'Kheda', 'Mahesana', 'Narmada', 'Navsari', 'Panch Mahals', 'Patan', 'Porbandar', 'Rajkot', 'Sabar Kantha',
    'Surat', 'Surendranagar', 'Tapi', 'Vadodara', 'Valsad', 'Ambala', 'Bhiwani', 'Fatehabad', 'Gurgaon', 'Hisar',
    'Jhajjar', 'Jind', 'Kaithal', 'Karnal', 'Kurukshetra', 'Mahendragarh', 'Palwal', 'Panchkula', 'Panipat', 'Rewari',
    'Rohtak', 'Sirsa', 'Sonipat', 'Yamunanagar', 'Faridabad', 'Mewat', 'Kangra', 'Shimla', 'Sirmaur', 'Hamirpur', 'Mandi',
    'Chamba', 'Kinnaur', 'Kullu', 'Lahul And Spiti', 'Solan', 'Una', 'Bokaro', 'Chatra', 'Deoghar', 'Dhanbad', 'Dumka',
    'East Singhbum', 'Garhwa', 'Giridih', 'Godda', 'Gumla', 'Hazaribagh', 'Jamtara', 'Khunti', 'Koderma', 'Latehar',
    'Lohardaga', 'Pakur', 'Palamu', 'Ramgarh', 'Ranchi', 'Sahebganj', 'Saraikela Kharsawan', 'Simdega', 'West Singhbhum',
    'Ballari', 'Bangalore Rural', 'Belagavi', 'Bengaluru Urban', 'Chamarajanagara', 'Chikkaballapura', 'Chikkamagaluru',
    'Chitradurga', 'Dakshina Kannada', 'Davangere', 'Dharwad', 'Gadag', 'Hassan', 'Haveri', 'Kodagu', 'Mandya', 'Mysuru',
    'Ramanagara', 'Shivamogga', 'Tumakuru', 'Udupi', 'Uttara Kannada', 'Bagalkote', 'Bidar', 'Kalaburagi', 'Kolar',
    'Koppal', 'Raichur', 'Vijayapura', 'Yadagiri', 'Alappuzha', 'Ernakulam', 'Idukki', 'Kannur', 'Kasaragod', 'Kollam',
    'Kottayam', 'Kozhikode', 'Malappuram', 'Palakkad', 'Pathanamthitta', 'Thiruvananthapuram', 'Thrissur', 'Wayanad',
    'Alirajpur', 'Anuppur', 'Ashoknagar', 'Balaghat', 'Barwani', 'Betul', 'Bhind', 'Bhopal', 'Burhanpur', 'Chhatarpur',
    'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dindori', 'Guna', 'Gwalior', 'Harda', 'Hoshangabad', 'Indore',
    'Jabalpur', 'Jhabua', 'Katni', 'Khandwa', 'Khargone', 'Mandla', 'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch',
    'Panna', 'Raisen', 'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur',
    'Shivpuri', 'Sidhi', 'Singrauli', 'Tikamgarh', 'Ujjain', 'Umaria',"Ajmer", "Alwar", "Banswara", "Baran", "Barmer", "Bharatpur",
    "Bhilwara", "Bikaner", "Bundi", "Chittorgarh", "Churu", "Dausa", "Dholpur", "Dungarpur", "Hanumangarh", "Jaipur", "Jaisalmer", 
    "Jalore", "Jhalawar", "Jhunjhunu", "Jodhpur", "Karauli", "Kota", "Nagaur", "Pali", "Pratapgarh", "Raj"

]

crop_names = [
    'Arecanut', 'Arhar/Tur', 'Bajra', 'Banana', 'Cashewnut', 'Castor Seed', 'Coriander', 'Cotton(Lint)', 'Dry Chillies',
    'Garlic', 'Ginger', 'Gram', 'Groundnut', 'Horse-Gram', 'Jowar', 'Linseed', 'Maize', 'Mesta', 'Moong(Green Gram)',
    'Niger Seed', 'Onion', 'Other Rabi Pulses', 'Other Kharif Pulses', 'Potato', 'Ragi', 'Rapeseed & Mustard', 'Rice',
    'Safflower', 'Sesamum', 'Small Millets', 'Soyabean', 'Sugarcane', 'Sunflower', 'Sweet Potato', 'Tapioca', 'Tobacco',
    'Turmeric', 'Urad', 'Wheat', 'Black Pepper', 'Jute', 'Masoor', 'Peas & Beans (Pulses)', 'Barley', 'Khesari', 'Sannhamp',
    'Guar Seed', 'Moth', 'Other Cereals', 'Other Oilseeds', 'Cardamom', 'Cowpea(Lobia)', 'Other Summer Pulses'
]

# Crop Mapping
crop_mapping = {crop: idx for idx, crop in enumerate(crop_names)}

# Generate mappings automatically
state_mapping = {state: idx for idx, state in enumerate(states)}
district_mapping = {district: idx for idx, district in enumerate(districts)}
# Crop Mapping
crop_mapping = {crop: idx for idx, crop in enumerate(crop_names)}

soil_mapping = {
    'Red and Yellow': 0, 'Red': 1, 'alluvial': 2, 'Black': 3,
    'laterite': 4, 'Desert': 5, 'Mountain': 6, 'Alluvial': 7
}
season_mapping = {
    'Whole Year': 0, 'Monsoon': 1, 'Winter': 2, 'Autumn': 3, 'Summer': 4
}

# Streamlit app
st.title("🌾 Crop Yield Prediction App")

year = st.number_input("Enter Year", min_value=2000, max_value=2025, value=2022)
state = st.selectbox("Select State", list(state_mapping.keys()))
district_name = st.selectbox("Select District", list(district_mapping.keys()))
season = st.selectbox("Select Season", list(season_mapping.keys()))
crop_name = st.selectbox("Select Crop", crop_names)
area = st.number_input("Enter Area (in Hectares)", min_value=0.0, value=10.0)
annual_rainfall = st.number_input("Enter Annual Rainfall (in mm)", min_value=0.0, value=1000.0)
soil_type = st.selectbox("Select Soil Type", list(soil_mapping.keys()))

# When predict button is clicked
if st.button('Predict Yield'):
    try:
        state_encoded = state_mapping[state]
        district_encoded = district_mapping[district_name]
        crop_encoded = crop_mapping[crop_name]
        soil_encoded = soil_mapping[soil_type]
        season_encoded = season_mapping[season]

        # Create input DataFrame
        input_data = pd.DataFrame([[
            year, state_encoded, district_encoded, season_encoded, crop_encoded, area, annual_rainfall, soil_encoded
        ]], columns=['year', 'state', 'district_name', 'season', 'crop_name', 'area', 'annual_rainfall', 'soil_type'])

        # Predict
        prediction = model.predict(input_data)
        st.success(f"🌾 Predicted Crop Yield: {prediction[0]:.2f} tons per hectare")

    except KeyError as e:
        st.error(f"Input Error: {e}. Please enter correct spelling/state/district/crop.")
