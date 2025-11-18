import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_india_network_dataset(num_records=10000):
    """Create a realistic India-focused mobile network performance dataset with comprehensive coverage"""
    
    # Comprehensive Indian cities - at least 5 cities per state/UT
    indian_locations = [
        # Andhra Pradesh
        {'city': 'Visakhapatnam', 'state': 'Andhra Pradesh', 'tier': 1, 'download_base': 42, 'upload_base': 11, 'latency_base': 38, '5g_penetration': 0.30},
        {'city': 'Vijayawada', 'state': 'Andhra Pradesh', 'tier': 2, 'download_base': 35, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.18},
        {'city': 'Guntur', 'state': 'Andhra Pradesh', 'tier': 2, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.15},
        {'city': 'Tirupati', 'state': 'Andhra Pradesh', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.12},
        {'city': 'Nellore', 'state': 'Andhra Pradesh', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.10},
        {'city': 'Kakinada', 'state': 'Andhra Pradesh', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 51, '5g_penetration': 0.11},
        
        # Arunachal Pradesh
        {'city': 'Itanagar', 'state': 'Arunachal Pradesh', 'tier': 3, 'download_base': 22, 'upload_base': 5, 'latency_base': 65, '5g_penetration': 0.05},
        {'city': 'Naharlagun', 'state': 'Arunachal Pradesh', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 68, '5g_penetration': 0.04},
        {'city': 'Pasighat', 'state': 'Arunachal Pradesh', 'tier': 3, 'download_base': 18, 'upload_base': 4, 'latency_base': 72, '5g_penetration': 0.03},
        {'city': 'Tezpur', 'state': 'Arunachal Pradesh', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 70, '5g_penetration': 0.03},
        {'city': 'Bomdila', 'state': 'Arunachal Pradesh', 'tier': 3, 'download_base': 17, 'upload_base': 3, 'latency_base': 75, '5g_penetration': 0.02},
        
        # Assam
        {'city': 'Guwahati', 'state': 'Assam', 'tier': 2, 'download_base': 35, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.20},
        {'city': 'Silchar', 'state': 'Assam', 'tier': 3, 'download_base': 26, 'upload_base': 6, 'latency_base': 55, '5g_penetration': 0.08},
        {'city': 'Dibrugarh', 'state': 'Assam', 'tier': 3, 'download_base': 25, 'upload_base': 6, 'latency_base': 57, '5g_penetration': 0.07},
        {'city': 'Jorhat', 'state': 'Assam', 'tier': 3, 'download_base': 24, 'upload_base': 5, 'latency_base': 58, '5g_penetration': 0.07},
        {'city': 'Nagaon', 'state': 'Assam', 'tier': 3, 'download_base': 22, 'upload_base': 5, 'latency_base': 62, '5g_penetration': 0.06},
        
        # Bihar
        {'city': 'Patna', 'state': 'Bihar', 'tier': 1, 'download_base': 36, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.15},
        {'city': 'Gaya', 'state': 'Bihar', 'tier': 3, 'download_base': 25, 'upload_base': 6, 'latency_base': 58, '5g_penetration': 0.07},
        {'city': 'Bhagalpur', 'state': 'Bihar', 'tier': 3, 'download_base': 24, 'upload_base': 5, 'latency_base': 60, '5g_penetration': 0.06},
        {'city': 'Muzaffarpur', 'state': 'Bihar', 'tier': 3, 'download_base': 26, 'upload_base': 6, 'latency_base': 56, '5g_penetration': 0.08},
        {'city': 'Darbhanga', 'state': 'Bihar', 'tier': 3, 'download_base': 23, 'upload_base': 5, 'latency_base': 61, '5g_penetration': 0.06},
        
        # Chhattisgarh
        {'city': 'Raipur', 'state': 'Chhattisgarh', 'tier': 2, 'download_base': 33, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Bhilai', 'state': 'Chhattisgarh', 'tier': 2, 'download_base': 31, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.14},
        {'city': 'Bilaspur', 'state': 'Chhattisgarh', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 53, '5g_penetration': 0.11},
        {'city': 'Korba', 'state': 'Chhattisgarh', 'tier': 3, 'download_base': 26, 'upload_base': 6, 'latency_base': 56, '5g_penetration': 0.09},
        {'city': 'Durg', 'state': 'Chhattisgarh', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.12},
        
        # Delhi
        {'city': 'New Delhi', 'state': 'Delhi', 'tier': 1, 'download_base': 48, 'upload_base': 13, 'latency_base': 34, '5g_penetration': 0.38},
        {'city': 'South Delhi', 'state': 'Delhi', 'tier': 1, 'download_base': 47, 'upload_base': 12, 'latency_base': 35, '5g_penetration': 0.37},
        {'city': 'East Delhi', 'state': 'Delhi', 'tier': 1, 'download_base': 44, 'upload_base': 11, 'latency_base': 37, '5g_penetration': 0.34},
        {'city': 'North Delhi', 'state': 'Delhi', 'tier': 1, 'download_base': 45, 'upload_base': 11, 'latency_base': 36, '5g_penetration': 0.35},
        {'city': 'West Delhi', 'state': 'Delhi', 'tier': 1, 'download_base': 46, 'upload_base': 12, 'latency_base': 35, '5g_penetration': 0.36},
        
        # Goa
        {'city': 'Panaji', 'state': 'Goa', 'tier': 2, 'download_base': 38, 'upload_base': 10, 'latency_base': 42, '5g_penetration': 0.25},
        {'city': 'Vasco da Gama', 'state': 'Goa', 'tier': 3, 'download_base': 35, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.20},
        {'city': 'Margao', 'state': 'Goa', 'tier': 3, 'download_base': 36, 'upload_base': 9, 'latency_base': 44, '5g_penetration': 0.22},
        {'city': 'Mapusa', 'state': 'Goa', 'tier': 3, 'download_base': 34, 'upload_base': 8, 'latency_base': 46, '5g_penetration': 0.18},
        {'city': 'Ponda', 'state': 'Goa', 'tier': 3, 'download_base': 33, 'upload_base': 8, 'latency_base': 47, '5g_penetration': 0.17},
        
        # Gujarat
        {'city': 'Ahmedabad', 'state': 'Gujarat', 'tier': 1, 'download_base': 44, 'upload_base': 11, 'latency_base': 37, '5g_penetration': 0.32},
        {'city': 'Surat', 'state': 'Gujarat', 'tier': 1, 'download_base': 40, 'upload_base': 10, 'latency_base': 40, '5g_penetration': 0.28},
        {'city': 'Vadodara', 'state': 'Gujarat', 'tier': 2, 'download_base': 38, 'upload_base': 9, 'latency_base': 43, '5g_penetration': 0.24},
        {'city': 'Rajkot', 'state': 'Gujarat', 'tier': 2, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.22},
        {'city': 'Bhavnagar', 'state': 'Gujarat', 'tier': 3, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Jamnagar', 'state': 'Gujarat', 'tier': 3, 'download_base': 33, 'upload_base': 8, 'latency_base': 47, '5g_penetration': 0.17},
        
        # Haryana
        {'city': 'Faridabad', 'state': 'Haryana', 'tier': 1, 'download_base': 43, 'upload_base': 11, 'latency_base': 38, '5g_penetration': 0.30},
        {'city': 'Gurgaon', 'state': 'Haryana', 'tier': 1, 'download_base': 47, 'upload_base': 12, 'latency_base': 35, '5g_penetration': 0.36},
        {'city': 'Panipat', 'state': 'Haryana', 'tier': 2, 'download_base': 34, 'upload_base': 8, 'latency_base': 46, '5g_penetration': 0.19},
        {'city': 'Ambala', 'state': 'Haryana', 'tier': 3, 'download_base': 31, 'upload_base': 7, 'latency_base': 49, '5g_penetration': 0.14},
        {'city': 'Rohtak', 'state': 'Haryana', 'tier': 3, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.15},
        {'city': 'Hisar', 'state': 'Haryana', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.13},
        
        # Himachal Pradesh
        {'city': 'Shimla', 'state': 'Himachal Pradesh', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 53, '5g_penetration': 0.12},
        {'city': 'Dharamshala', 'state': 'Himachal Pradesh', 'tier': 3, 'download_base': 26, 'upload_base': 6, 'latency_base': 56, '5g_penetration': 0.10},
        {'city': 'Mandi', 'state': 'Himachal Pradesh', 'tier': 3, 'download_base': 24, 'upload_base': 6, 'latency_base': 59, '5g_penetration': 0.08},
        {'city': 'Solan', 'state': 'Himachal Pradesh', 'tier': 3, 'download_base': 27, 'upload_base': 7, 'latency_base': 54, '5g_penetration': 0.11},
        {'city': 'Kullu', 'state': 'Himachal Pradesh', 'tier': 3, 'download_base': 23, 'upload_base': 5, 'latency_base': 61, '5g_penetration': 0.07},
        
        # Jharkhand
        {'city': 'Ranchi', 'state': 'Jharkhand', 'tier': 2, 'download_base': 33, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Jamshedpur', 'state': 'Jharkhand', 'tier': 2, 'download_base': 32, 'upload_base': 8, 'latency_base': 49, '5g_penetration': 0.15},
        {'city': 'Dhanbad', 'state': 'Jharkhand', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 53, '5g_penetration': 0.11},
        {'city': 'Bokaro', 'state': 'Jharkhand', 'tier': 3, 'download_base': 27, 'upload_base': 6, 'latency_base': 54, '5g_penetration': 0.10},
        {'city': 'Deoghar', 'state': 'Jharkhand', 'tier': 3, 'download_base': 25, 'upload_base': 6, 'latency_base': 57, '5g_penetration': 0.08},
        
        # Karnataka
        {'city': 'Bangalore', 'state': 'Karnataka', 'tier': 1, 'download_base': 50, 'upload_base': 13, 'latency_base': 32, '5g_penetration': 0.40},
        {'city': 'Mysore', 'state': 'Karnataka', 'tier': 2, 'download_base': 38, 'upload_base': 10, 'latency_base': 43, '5g_penetration': 0.24},
        {'city': 'Mangalore', 'state': 'Karnataka', 'tier': 2, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.21},
        {'city': 'Hubli', 'state': 'Karnataka', 'tier': 3, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Belgaum', 'state': 'Karnataka', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.14},
        {'city': 'Gulbarga', 'state': 'Karnataka', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 51, '5g_penetration': 0.12},
        
        # Kerala
        {'city': 'Thiruvananthapuram', 'state': 'Kerala', 'tier': 2, 'download_base': 38, 'upload_base': 10, 'latency_base': 43, '5g_penetration': 0.24},
        {'city': 'Kochi', 'state': 'Kerala', 'tier': 1, 'download_base': 42, 'upload_base': 11, 'latency_base': 39, '5g_penetration': 0.28},
        {'city': 'Kozhikode', 'state': 'Kerala', 'tier': 2, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.21},
        {'city': 'Thrissur', 'state': 'Kerala', 'tier': 3, 'download_base': 34, 'upload_base': 8, 'latency_base': 47, '5g_penetration': 0.18},
        {'city': 'Kannur', 'state': 'Kerala', 'tier': 3, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        
        # Madhya Pradesh
        {'city': 'Indore', 'state': 'Madhya Pradesh', 'tier': 1, 'download_base': 40, 'upload_base': 10, 'latency_base': 41, '5g_penetration': 0.26},
        {'city': 'Bhopal', 'state': 'Madhya Pradesh', 'tier': 2, 'download_base': 37, 'upload_base': 9, 'latency_base': 44, '5g_penetration': 0.22},
        {'city': 'Jabalpur', 'state': 'Madhya Pradesh', 'tier': 2, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Gwalior', 'state': 'Madhya Pradesh', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.14},
        {'city': 'Ujjain', 'state': 'Madhya Pradesh', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.12},
        
        # Maharashtra
        {'city': 'Mumbai', 'state': 'Maharashtra', 'tier': 1, 'download_base': 48, 'upload_base': 12, 'latency_base': 35, '5g_penetration': 0.37},
        {'city': 'Pune', 'state': 'Maharashtra', 'tier': 1, 'download_base': 46, 'upload_base': 12, 'latency_base': 36, '5g_penetration': 0.34},
        {'city': 'Nagpur', 'state': 'Maharashtra', 'tier': 2, 'download_base': 38, 'upload_base': 9, 'latency_base': 43, '5g_penetration': 0.24},
        {'city': 'Nashik', 'state': 'Maharashtra', 'tier': 2, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.21},
        {'city': 'Aurangabad', 'state': 'Maharashtra', 'tier': 3, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Thane', 'state': 'Maharashtra', 'tier': 1, 'download_base': 44, 'upload_base': 11, 'latency_base': 37, '5g_penetration': 0.32},
        
        # Manipur
        {'city': 'Imphal', 'state': 'Manipur', 'tier': 3, 'download_base': 24, 'upload_base': 6, 'latency_base': 60, '5g_penetration': 0.07},
        {'city': 'Thoubal', 'state': 'Manipur', 'tier': 3, 'download_base': 21, 'upload_base': 5, 'latency_base': 65, '5g_penetration': 0.05},
        {'city': 'Bishnupur', 'state': 'Manipur', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 67, '5g_penetration': 0.04},
        {'city': 'Churachandpur', 'state': 'Manipur', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 69, '5g_penetration': 0.04},
        {'city': 'Ukhrul', 'state': 'Manipur', 'tier': 3, 'download_base': 18, 'upload_base': 4, 'latency_base': 71, '5g_penetration': 0.03},
        
        # Meghalaya
        {'city': 'Shillong', 'state': 'Meghalaya', 'tier': 3, 'download_base': 26, 'upload_base': 6, 'latency_base': 56, '5g_penetration': 0.09},
        {'city': 'Tura', 'state': 'Meghalaya', 'tier': 3, 'download_base': 22, 'upload_base': 5, 'latency_base': 63, '5g_penetration': 0.06},
        {'city': 'Jowai', 'state': 'Meghalaya', 'tier': 3, 'download_base': 21, 'upload_base': 5, 'latency_base': 65, '5g_penetration': 0.05},
        {'city': 'Nongpoh', 'state': 'Meghalaya', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 67, '5g_penetration': 0.04},
        {'city': 'Nongstoin', 'state': 'Meghalaya', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 69, '5g_penetration': 0.04},
        
        # Mizoram
        {'city': 'Aizawl', 'state': 'Mizoram', 'tier': 3, 'download_base': 23, 'upload_base': 5, 'latency_base': 62, '5g_penetration': 0.06},
        {'city': 'Lunglei', 'state': 'Mizoram', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 67, '5g_penetration': 0.04},
        {'city': 'Champhai', 'state': 'Mizoram', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 69, '5g_penetration': 0.04},
        {'city': 'Serchhip', 'state': 'Mizoram', 'tier': 3, 'download_base': 18, 'upload_base': 4, 'latency_base': 71, '5g_penetration': 0.03},
        {'city': 'Kolasib', 'state': 'Mizoram', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 70, '5g_penetration': 0.03},
        
        # Nagaland
        {'city': 'Kohima', 'state': 'Nagaland', 'tier': 3, 'download_base': 22, 'upload_base': 5, 'latency_base': 64, '5g_penetration': 0.06},
        {'city': 'Dimapur', 'state': 'Nagaland', 'tier': 3, 'download_base': 24, 'upload_base': 6, 'latency_base': 60, '5g_penetration': 0.07},
        {'city': 'Mokokchung', 'state': 'Nagaland', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 67, '5g_penetration': 0.04},
        {'city': 'Tuensang', 'state': 'Nagaland', 'tier': 3, 'download_base': 18, 'upload_base': 4, 'latency_base': 72, '5g_penetration': 0.03},
        {'city': 'Wokha', 'state': 'Nagaland', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 70, '5g_penetration': 0.03},
        
        # Odisha
        {'city': 'Bhubaneswar', 'state': 'Odisha', 'tier': 2, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.21},
        {'city': 'Cuttack', 'state': 'Odisha', 'tier': 2, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Rourkela', 'state': 'Odisha', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 53, '5g_penetration': 0.11},
        {'city': 'Berhampur', 'state': 'Odisha', 'tier': 3, 'download_base': 26, 'upload_base': 6, 'latency_base': 56, '5g_penetration': 0.09},
        {'city': 'Sambalpur', 'state': 'Odisha', 'tier': 3, 'download_base': 25, 'upload_base': 6, 'latency_base': 58, '5g_penetration': 0.08},
        
        # Punjab
        {'city': 'Ludhiana', 'state': 'Punjab', 'tier': 2, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.21},
        {'city': 'Amritsar', 'state': 'Punjab', 'tier': 2, 'download_base': 35, 'upload_base': 9, 'latency_base': 46, '5g_penetration': 0.20},
        {'city': 'Jalandhar', 'state': 'Punjab', 'tier': 2, 'download_base': 33, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.18},
        {'city': 'Patiala', 'state': 'Punjab', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.14},
        {'city': 'Bathinda', 'state': 'Punjab', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 53, '5g_penetration': 0.12},
        
        # Rajasthan
        {'city': 'Jaipur', 'state': 'Rajasthan', 'tier': 1, 'download_base': 40, 'upload_base': 10, 'latency_base': 41, '5g_penetration': 0.26},
        {'city': 'Jodhpur', 'state': 'Rajasthan', 'tier': 2, 'download_base': 33, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.17},
        {'city': 'Udaipur', 'state': 'Rajasthan', 'tier': 2, 'download_base': 32, 'upload_base': 8, 'latency_base': 49, '5g_penetration': 0.16},
        {'city': 'Kota', 'state': 'Rajasthan', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.14},
        {'city': 'Ajmer', 'state': 'Rajasthan', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 51, '5g_penetration': 0.13},
        {'city': 'Bikaner', 'state': 'Rajasthan', 'tier': 3, 'download_base': 27, 'upload_base': 6, 'latency_base': 54, '5g_penetration': 0.11},
        
        # Sikkim
        {'city': 'Gangtok', 'state': 'Sikkim', 'tier': 3, 'download_base': 25, 'upload_base': 6, 'latency_base': 58, '5g_penetration': 0.08},
        {'city': 'Namchi', 'state': 'Sikkim', 'tier': 3, 'download_base': 22, 'upload_base': 5, 'latency_base': 63, '5g_penetration': 0.06},
        {'city': 'Mangan', 'state': 'Sikkim', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 67, '5g_penetration': 0.04},
        {'city': 'Gyalshing', 'state': 'Sikkim', 'tier': 3, 'download_base': 21, 'upload_base': 5, 'latency_base': 65, '5g_penetration': 0.05},
        {'city': 'Rangpo', 'state': 'Sikkim', 'tier': 3, 'download_base': 23, 'upload_base': 5, 'latency_base': 61, '5g_penetration': 0.06},
        
        # Tamil Nadu
        {'city': 'Chennai', 'state': 'Tamil Nadu', 'tier': 1, 'download_base': 45, 'upload_base': 11, 'latency_base': 37, '5g_penetration': 0.33},
        {'city': 'Coimbatore', 'state': 'Tamil Nadu', 'tier': 2, 'download_base': 38, 'upload_base': 10, 'latency_base': 43, '5g_penetration': 0.24},
        {'city': 'Madurai', 'state': 'Tamil Nadu', 'tier': 2, 'download_base': 34, 'upload_base': 8, 'latency_base': 47, '5g_penetration': 0.19},
        {'city': 'Tiruchirappalli', 'state': 'Tamil Nadu', 'tier': 3, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Salem', 'state': 'Tamil Nadu', 'tier': 3, 'download_base': 31, 'upload_base': 7, 'latency_base': 49, '5g_penetration': 0.15},
        {'city': 'Tirunelveli', 'state': 'Tamil Nadu', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 51, '5g_penetration': 0.13},
        
        # Telangana
        {'city': 'Hyderabad', 'state': 'Telangana', 'tier': 1, 'download_base': 48, 'upload_base': 12, 'latency_base': 33, '5g_penetration': 0.38},
        {'city': 'Warangal', 'state': 'Telangana', 'tier': 2, 'download_base': 33, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.17},
        {'city': 'Nizamabad', 'state': 'Telangana', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.12},
        {'city': 'Karimnagar', 'state': 'Telangana', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 53, '5g_penetration': 0.11},
        {'city': 'Khammam', 'state': 'Telangana', 'tier': 3, 'download_base': 27, 'upload_base': 6, 'latency_base': 54, '5g_penetration': 0.10},
        
        # Tripura
        {'city': 'Agartala', 'state': 'Tripura', 'tier': 3, 'download_base': 26, 'upload_base': 6, 'latency_base': 56, '5g_penetration': 0.09},
        {'city': 'Udaipur', 'state': 'Tripura', 'tier': 3, 'download_base': 22, 'upload_base': 5, 'latency_base': 63, '5g_penetration': 0.06},
        {'city': 'Dharmanagar', 'state': 'Tripura', 'tier': 3, 'download_base': 21, 'upload_base': 5, 'latency_base': 65, '5g_penetration': 0.05},
        {'city': 'Kailasahar', 'state': 'Tripura', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 67, '5g_penetration': 0.04},
        {'city': 'Ambassa', 'state': 'Tripura', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 69, '5g_penetration': 0.04},
        
        # Uttar Pradesh
        {'city': 'Lucknow', 'state': 'Uttar Pradesh', 'tier': 1, 'download_base': 38, 'upload_base': 9, 'latency_base': 43, '5g_penetration': 0.24},
        {'city': 'Kanpur', 'state': 'Uttar Pradesh', 'tier': 1, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.21},
        {'city': 'Ghaziabad', 'state': 'Uttar Pradesh', 'tier': 2, 'download_base': 40, 'upload_base': 10, 'latency_base': 41, '5g_penetration': 0.27},
        {'city': 'Agra', 'state': 'Uttar Pradesh', 'tier': 2, 'download_base': 34, 'upload_base': 8, 'latency_base': 47, '5g_penetration': 0.19},
        {'city': 'Varanasi', 'state': 'Uttar Pradesh', 'tier': 2, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Meerut', 'state': 'Uttar Pradesh', 'tier': 2, 'download_base': 33, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.17},
        {'city': 'Allahabad', 'state': 'Uttar Pradesh', 'tier': 2, 'download_base': 31, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.15},
        {'city': 'Bareilly', 'state': 'Uttar Pradesh', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 53, '5g_penetration': 0.11},
        
        # Uttarakhand
        {'city': 'Dehradun', 'state': 'Uttarakhand', 'tier': 2, 'download_base': 34, 'upload_base': 8, 'latency_base': 47, '5g_penetration': 0.19},
        {'city': 'Haridwar', 'state': 'Uttarakhand', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.14},
        {'city': 'Roorkee', 'state': 'Uttarakhand', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 51, '5g_penetration': 0.13},
        {'city': 'Haldwani', 'state': 'Uttarakhand', 'tier': 3, 'download_base': 27, 'upload_base': 6, 'latency_base': 54, '5g_penetration': 0.11},
        {'city': 'Rudrapur', 'state': 'Uttarakhand', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.12},
        
        # West Bengal
        {'city': 'Kolkata', 'state': 'West Bengal', 'tier': 1, 'download_base': 42, 'upload_base': 10, 'latency_base': 40, '5g_penetration': 0.29},
        {'city': 'Howrah', 'state': 'West Bengal', 'tier': 2, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.21},
        {'city': 'Durgapur', 'state': 'West Bengal', 'tier': 2, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Siliguri', 'state': 'West Bengal', 'tier': 2, 'download_base': 31, 'upload_base': 7, 'latency_base': 49, '5g_penetration': 0.15},
        {'city': 'Asansol', 'state': 'West Bengal', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 51, '5g_penetration': 0.13},
        {'city': 'Kharagpur', 'state': 'West Bengal', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.12},
        
        # Union Territories
        # Andaman and Nicobar Islands
        {'city': 'Port Blair', 'state': 'Andaman and Nicobar Islands', 'tier': 3, 'download_base': 24, 'upload_base': 6, 'latency_base': 60, '5g_penetration': 0.07},
        {'city': 'Car Nicobar', 'state': 'Andaman and Nicobar Islands', 'tier': 3, 'download_base': 18, 'upload_base': 4, 'latency_base': 75, '5g_penetration': 0.02},
        {'city': 'Diglipur', 'state': 'Andaman and Nicobar Islands', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 70, '5g_penetration': 0.03},
        {'city': 'Rangat', 'state': 'Andaman and Nicobar Islands', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 72, '5g_penetration': 0.03},
        {'city': 'Mayabunder', 'state': 'Andaman and Nicobar Islands', 'tier': 3, 'download_base': 17, 'upload_base': 3, 'latency_base': 78, '5g_penetration': 0.02},
        
        # Chandigarh
        {'city': 'Chandigarh Sector 17', 'state': 'Chandigarh', 'tier': 1, 'download_base': 42, 'upload_base': 11, 'latency_base': 38, '5g_penetration': 0.30},
        {'city': 'Chandigarh Sector 22', 'state': 'Chandigarh', 'tier': 1, 'download_base': 41, 'upload_base': 10, 'latency_base': 39, '5g_penetration': 0.29},
        {'city': 'Chandigarh Sector 35', 'state': 'Chandigarh', 'tier': 1, 'download_base': 40, 'upload_base': 10, 'latency_base': 40, '5g_penetration': 0.28},
        {'city': 'Chandigarh Sector 43', 'state': 'Chandigarh', 'tier': 1, 'download_base': 41, 'upload_base': 10, 'latency_base': 39, '5g_penetration': 0.29},
        {'city': 'Chandigarh Manimajra', 'state': 'Chandigarh', 'tier': 2, 'download_base': 38, 'upload_base': 9, 'latency_base': 43, '5g_penetration': 0.25},
        
        # Dadra and Nagar Haveli and Daman and Diu
        {'city': 'Daman', 'state': 'Dadra and Nagar Haveli and Daman and Diu', 'tier': 3, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Diu', 'state': 'Dadra and Nagar Haveli and Daman and Diu', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.14},
        {'city': 'Silvassa', 'state': 'Dadra and Nagar Haveli and Daman and Diu', 'tier': 3, 'download_base': 31, 'upload_base': 7, 'latency_base': 49, '5g_penetration': 0.15},
        {'city': 'Amli', 'state': 'Dadra and Nagar Haveli and Daman and Diu', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.12},
        {'city': 'Naroli', 'state': 'Dadra and Nagar Haveli and Daman and Diu', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 51, '5g_penetration': 0.13},
        
        # Jammu and Kashmir
        {'city': 'Srinagar', 'state': 'Jammu and Kashmir', 'tier': 2, 'download_base': 30, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.13},
        {'city': 'Jammu', 'state': 'Jammu and Kashmir', 'tier': 2, 'download_base': 32, 'upload_base': 8, 'latency_base': 48, '5g_penetration': 0.16},
        {'city': 'Anantnag', 'state': 'Jammu and Kashmir', 'tier': 3, 'download_base': 26, 'upload_base': 6, 'latency_base': 56, '5g_penetration': 0.09},
        {'city': 'Baramulla', 'state': 'Jammu and Kashmir', 'tier': 3, 'download_base': 25, 'upload_base': 6, 'latency_base': 58, '5g_penetration': 0.08},
        {'city': 'Udhampur', 'state': 'Jammu and Kashmir', 'tier': 3, 'download_base': 27, 'upload_base': 6, 'latency_base': 54, '5g_penetration': 0.10},
        
        # Ladakh
        {'city': 'Leh', 'state': 'Ladakh', 'tier': 3, 'download_base': 22, 'upload_base': 5, 'latency_base': 65, '5g_penetration': 0.06},
        {'city': 'Kargil', 'state': 'Ladakh', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 70, '5g_penetration': 0.04},
        {'city': 'Nubra', 'state': 'Ladakh', 'tier': 3, 'download_base': 18, 'upload_base': 4, 'latency_base': 75, '5g_penetration': 0.03},
        {'city': 'Zanskar', 'state': 'Ladakh', 'tier': 3, 'download_base': 16, 'upload_base': 3, 'latency_base': 80, '5g_penetration': 0.02},
        {'city': 'Drass', 'state': 'Ladakh', 'tier': 3, 'download_base': 17, 'upload_base': 3, 'latency_base': 78, '5g_penetration': 0.02},
        
        # Lakshadweep
        {'city': 'Kavaratti', 'state': 'Lakshadweep', 'tier': 3, 'download_base': 20, 'upload_base': 4, 'latency_base': 70, '5g_penetration': 0.04},
        {'city': 'Agatti', 'state': 'Lakshadweep', 'tier': 3, 'download_base': 18, 'upload_base': 4, 'latency_base': 75, '5g_penetration': 0.03},
        {'city': 'Andrott', 'state': 'Lakshadweep', 'tier': 3, 'download_base': 17, 'upload_base': 3, 'latency_base': 77, '5g_penetration': 0.02},
        {'city': 'Minicoy', 'state': 'Lakshadweep', 'tier': 3, 'download_base': 19, 'upload_base': 4, 'latency_base': 72, '5g_penetration': 0.03},
        {'city': 'Amini', 'state': 'Lakshadweep', 'tier': 3, 'download_base': 18, 'upload_base': 4, 'latency_base': 74, '5g_penetration': 0.03},
        
        # Puducherry
        {'city': 'Puducherry City', 'state': 'Puducherry', 'tier': 2, 'download_base': 36, 'upload_base': 9, 'latency_base': 45, '5g_penetration': 0.21},
        {'city': 'Karaikal', 'state': 'Puducherry', 'tier': 3, 'download_base': 30, 'upload_base': 7, 'latency_base': 50, '5g_penetration': 0.14},
        {'city': 'Mahe', 'state': 'Puducherry', 'tier': 3, 'download_base': 29, 'upload_base': 7, 'latency_base': 51, '5g_penetration': 0.13},
        {'city': 'Yanam', 'state': 'Puducherry', 'tier': 3, 'download_base': 28, 'upload_base': 7, 'latency_base': 52, '5g_penetration': 0.12},
        {'city': 'Ozhukarai', 'state': 'Puducherry', 'tier': 3, 'download_base': 33, 'upload_base': 8, 'latency_base': 47, '5g_penetration': 0.17},
    ]
    
    print(f"📍 Total locations loaded: {len(indian_locations)}")
    print(f"🗺️ States/UTs covered: {len(set([loc['state'] for loc in indian_locations]))}")
    
    # Realistic Indian device distribution (based on market share)
    indian_devices = [
        # Premium segment (10%)
        'iPhone 15 Pro Max', 'iPhone 15 Pro', 'iPhone 15', 'iPhone 14 Pro', 'iPhone 14',
        'Samsung Galaxy S24 Ultra', 'Samsung Galaxy S23 Ultra', 'Samsung Galaxy S23',
        'OnePlus 12', 'OnePlus 11', 'Google Pixel 8 Pro',
        
        # Upper mid-range (20%)
        'Samsung Galaxy A54', 'Samsung Galaxy A34', 'Samsung Galaxy S21 FE',
        'OnePlus Nord 3', 'OnePlus Nord CE 3', 'OnePlus 11R',
        'Vivo V29 Pro', 'Vivo V27 Pro', 'Oppo Reno 11 Pro',
        'Google Pixel 7a', 'Google Pixel 6a', 'Motorola Edge 40',
        'Nothing Phone 2', 'Nothing Phone 1',
        
        # Mid-range (35%)
        'Xiaomi 13T', 'Xiaomi 12', 'Xiaomi 11T',
        'Realme 11 Pro+', 'Realme GT Neo 3', 'Realme 10 Pro+',
        'Vivo V29', 'Vivo T2 Pro', 'Vivo Y100',
        'Oppo Reno 10', 'Oppo F23', 'Oppo A78',
        'Samsung Galaxy M34', 'Samsung Galaxy M54', 'Samsung Galaxy F54',
        'Poco F5', 'Poco X5 Pro', 'Motorola Edge 30',
        'iQOO Neo 7', 'iQOO Z7 Pro',
        
        # Budget segment (35%)
        'Redmi Note 13 Pro', 'Redmi Note 13', 'Redmi Note 12 Pro', 'Redmi Note 12',
        'Redmi 13C', 'Redmi 12', 'Redmi A3',
        'Realme Narzo 60', 'Realme Narzo 50', 'Realme C55', 'Realme C53', 'Realme C35',
        'Samsung Galaxy A14', 'Samsung Galaxy A05s', 'Samsung Galaxy M14', 'Samsung Galaxy M13',
        'Poco M6 Pro', 'Poco M5', 'Poco C55',
        'Vivo Y27', 'Vivo Y17', 'Vivo Y16', 'Oppo A58', 'Oppo A18',
        'Motorola Moto G54', 'Motorola Moto G34', 'Motorola Moto G24',
        'Infinix Hot 30', 'Infinix Note 30', 'Tecno Spark 10 Pro',
        'Lava Agni 2', 'Micromax In Note 2',
    ]
    
    # Indian network operators
    indian_carriers = ['Jio', 'Airtel', 'Vi (Vodafone Idea)', 'BSNL']
    carrier_weights = [0.40, 0.35, 0.20, 0.05]  # Market share approximation
    
    # Realistic network type distribution for India
    network_types = ['5G', '4G+', '4G', '3G', '2G']
    
    # Frequency bands used in India
    indian_bands = [
        # 5G bands
        'n78 (3500 MHz)', 'n77 (3300 MHz)', 'n258 (mmWave)',
        # 4G bands
        'B3 (1800 MHz)', 'B5 (850 MHz)', 'B8 (900 MHz)', 'B40 (2300 MHz)',
        'B41 (2500 MHz)', 'B1 (2100 MHz)',
        # 3G bands
        'B1 (2100 MHz 3G)', 'B5 (850 MHz 3G)', 'B8 (900 MHz 3G)'
    ]
    
    data = []
    
    for i in range(num_records):
        # Select location
        loc = np.random.choice(indian_locations)
        five_g_penetration = loc['5g_penetration']
        tier = loc['tier']
        
        # Network type distribution based on 5G penetration and tier
        if five_g_penetration > 0.30:
            network_probs = [0.35, 0.35, 0.25, 0.04, 0.01]
        elif five_g_penetration > 0.15:
            network_probs = [0.20, 0.30, 0.40, 0.08, 0.02]
        else:
            network_probs = [0.10, 0.25, 0.50, 0.12, 0.03]
        
        network_type = np.random.choice(network_types, p=network_probs)
        
        # Carrier selection
        carrier = np.random.choice(indian_carriers, p=carrier_weights)
        
        # Base performance
        base_download = loc['download_base']
        base_upload = loc['upload_base']
        base_latency = loc['latency_base']
        
        # Network type multipliers (realistic for India)
        network_multipliers = {
            '5G': (2.5, 2.0, 0.6),
            '4G+': (1.5, 1.3, 0.8),
            '4G': (1.0, 1.0, 1.0),
            '3G': (0.15, 0.12, 2.5),
            '2G': (0.03, 0.02, 5.0)
        }
        
        mult_dl, mult_ul, mult_lat = network_multipliers[network_type]
        
        # Apply variations with realistic distribution
        download_speed = max(0.5, np.random.lognormal(np.log(base_download * mult_dl), 0.6))
        upload_speed = max(0.2, np.random.lognormal(np.log(base_upload * mult_ul), 0.65))
        latency = max(10, np.random.lognormal(np.log(base_latency * mult_lat), 0.5))
        
        # Signal strength (India has more variation)
        signal_strength = np.random.normal(-85, 18)
        signal_factor = max(0.1, min(1.3, (signal_strength + 110) / 40))
        
        download_speed *= signal_factor
        upload_speed *= signal_factor
        latency /= (signal_factor * 0.8)  # Less impact on latency
        
        # Time-based variations (Indian context)
        current_hour = np.random.randint(0, 24)
        if 9 <= current_hour <= 11 or 19 <= current_hour <= 22:  # Peak hours in India
            download_speed *= np.random.uniform(0.4, 0.7)
            upload_speed *= np.random.uniform(0.35, 0.65)
            latency *= np.random.uniform(1.3, 2.0)
        elif 2 <= current_hour <= 6:  # Night hours
            download_speed *= np.random.uniform(1.2, 1.6)
            upload_speed *= np.random.uniform(1.1, 1.5)
            latency *= np.random.uniform(0.7, 0.9)
        
        # Jitter calculation
        base_jitter = latency * np.random.uniform(0.08, 0.20)
        jitter = max(0.5, np.random.exponential(base_jitter))
        
        # Device selection and capability
        device = np.random.choice(indian_devices)
        if any(x in device for x in ['iPhone', 'Galaxy S', 'OnePlus 12', 'OnePlus 11', 'Pixel 8']):
            download_speed *= np.random.uniform(1.05, 1.12)
            upload_speed *= np.random.uniform(1.03, 1.10)
            latency *= np.random.uniform(0.93, 0.98)
        elif any(x in device for x in ['Redmi', 'Realme C', 'Infinix', 'Tecno', 'Galaxy A0', 'Galaxy M1']):
            download_speed *= np.random.uniform(0.80, 0.90)
            upload_speed *= np.random.uniform(0.75, 0.88)
            latency *= np.random.uniform(1.08, 1.18)
        
        # Band selection based on network type
        if network_type == '5G':
            band = np.random.choice(['n78 (3500 MHz)', 'n77 (3300 MHz)', 'n258 (mmWave)'], p=[0.70, 0.25, 0.05])
        elif network_type in ['4G+', '4G']:
            band = np.random.choice(['B3 (1800 MHz)', 'B40 (2300 MHz)', 'B41 (2500 MHz)', 'B5 (850 MHz)'], p=[0.40, 0.30, 0.20, 0.10])
        else:
            band = np.random.choice(['B1 (2100 MHz 3G)', 'B8 (900 MHz 3G)', 'B5 (850 MHz 3G)'])
        
        record = {
            'Timestamp': datetime.now() - timedelta(hours=np.random.randint(0, 8760)),
            'City': loc['city'],
            'State': loc['state'],
            'City_Tier': tier,
            'Signal_Strength_dBm': round(signal_strength, 1),
            'Download_Speed_Mbps': round(max(0.1, download_speed), 2),
            'Upload_Speed_Mbps': round(max(0.1, upload_speed), 2),
            'Latency_ms': round(max(5, latency), 1),
            'Jitter_ms': round(max(0.2, jitter), 2),
            'Network_Type': network_type,
            'Device_Model': device,
            'Carrier': carrier,
            'Band': band,
            'Battery_Level_%': np.random.randint(10, 100),
            'Temperature_C': round(np.random.normal(35, 8), 1),  # Indian climate
            'Connected_Duration_min': round(np.random.exponential(45), 1),
            'Handover_Count': np.random.poisson(3),
            'Data_Usage_MB': round(np.random.exponential(350), 1),
            'Video_Streaming_Quality': np.random.choice(['240p', '360p', '480p', '720p', '1080p', '1440p'], 
                                                        p=[0.10, 0.20, 0.30, 0.25, 0.12, 0.03]),
            'VoLTE_Enabled': np.random.choice([True, False], p=[0.85, 0.15]),
            'Network_Congestion_Level': np.random.choice(['Low', 'Medium', 'High'], p=[0.40, 0.40, 0.20]),
            'Ping_to_Server_ms': round(max(15, latency + np.random.exponential(8)), 1),
            'Packet_Loss_%': round(np.random.exponential(0.8), 2),
            'Dropped_Connection': np.random.choice([True, False], p=[0.08, 0.92]),
            'Indoor_Outdoor': np.random.choice(['Indoor', 'Outdoor'], p=[0.60, 0.40])
        }
        data.append(record)
    
    return pd.DataFrame(data)

# Generate the India-focused dataset
print("🇮🇳 Generating India network performance dataset...")
df_india = create_india_network_dataset(30000)

# Save to CSV
df_india.to_csv('india_network_data.csv', index=False)

print("\n✅ India network dataset created: 'india_network_data.csv'")
print(f"📊 Total records: {len(df_india)}")
print(f"🏙️ Cities covered: {df_india['City'].nunique()}")
print(f"🗺️ States/UTs covered: {df_india['State'].nunique()}")
print(f"📱 Device models: {df_india['Device_Model'].nunique()}")
print(f"📶 Network types: {', '.join(df_india['Network_Type'].unique())}")
print(f"🏢 Carriers: {', '.join(df_india['Carrier'].unique())}")
print(f"📡 Frequency bands: {df_india['Band'].nunique()}")
print(f"\n📈 Performance Metrics:")
print(f"📥 Average Download Speed: {df_india['Download_Speed_Mbps'].mean():.1f} Mbps")
print(f"📤 Average Upload Speed: {df_india['Upload_Speed_Mbps'].mean():.1f} Mbps")
print(f"⏱️ Average Latency: {df_india['Latency_ms'].mean():.1f} ms")
print(f"\n📊 Network Distribution:")
print(f"5G Adoption: {(df_india['Network_Type'] == '5G').sum() / len(df_india) * 100:.1f}%")
print(f"4G+ Adoption: {(df_india['Network_Type'] == '4G+').sum() / len(df_india) * 100:.1f}%")
print(f"4G Adoption: {(df_india['Network_Type'] == '4G').sum() / len(df_india) * 100:.1f}%")
print(f"3G Adoption: {(df_india['Network_Type'] == '3G').sum() / len(df_india) * 100:.1f}%")
print(f"2G Adoption: {(df_india['Network_Type'] == '2G').sum() / len(df_india) * 100:.1f}%")
print("\n🎯 Top 10 Cities by Average Download Speed:")
top_cities = df_india.groupby('City')['Download_Speed_Mbps'].mean().sort_values(ascending=False).head(10)
for idx, (city, speed) in enumerate(top_cities.items(), 1):
    print(f"{idx}. {city}: {speed:.1f} Mbps")

print("\n🗺️ Top 10 States by Average Download Speed:")
top_states = df_india.groupby('State')['Download_Speed_Mbps'].mean().sort_values(ascending=False).head(10)
for idx, (state, speed) in enumerate(top_states.items(), 1):
    print(f"{idx}. {state}: {speed:.1f} Mbps")

print("\n📱 Top 10 Most Common Devices:")
top_devices = df_india['Device_Model'].value_counts().head(10)
for idx, (device, count) in enumerate(top_devices.items(), 1):
    print(f"{idx}. {device}: {count} records")

print("\n🏢 Carrier Distribution:")
carrier_dist = df_india['Carrier'].value_counts()
for carrier, count in carrier_dist.items():
    print(f"{carrier}: {count} records ({count/len(df_india)*100:.1f}%)")

print("\n🌡️ Temperature Statistics:")
print(f"Average: {df_india['Temperature_C'].mean():.1f}°C")
print(f"Min: {df_india['Temperature_C'].min():.1f}°C")
print(f"Max: {df_india['Temperature_C'].max():.1f}°C")

print("\n📶 Signal Strength Statistics:")
print(f"Average: {df_india['Signal_Strength_dBm'].mean():.1f} dBm")
print(f"Min: {df_india['Signal_Strength_dBm'].min():.1f} dBm")
print(f"Max: {df_india['Signal_Strength_dBm'].max():.1f} dBm")

print("\n✨ Dataset generation complete!")