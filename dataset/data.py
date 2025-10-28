import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_modern_global_network_dataset(num_records=10000):
    """Create a realistic modern global mobile network performance dataset"""
    
    # Comprehensive global cities with 2024 realistic performance characteristics
    global_locations = [
        # North America - High 5G penetration
        {'city': 'New York', 'country': 'USA', 'continent': 'North America', 'region': 'Northeast', 'download_base': 250, 'upload_base': 45, 'latency_base': 12, '5g_penetration': 0.85},
        {'city': 'Los Angeles', 'country': 'USA', 'continent': 'North America', 'region': 'West', 'download_base': 240, 'upload_base': 42, 'latency_base': 15, '5g_penetration': 0.82},
        {'city': 'Chicago', 'country': 'USA', 'continent': 'North America', 'region': 'Midwest', 'download_base': 230, 'upload_base': 40, 'latency_base': 14, '5g_penetration': 0.80},
        {'city': 'San Francisco', 'country': 'USA', 'continent': 'North America', 'region': 'West', 'download_base': 260, 'upload_base': 48, 'latency_base': 10, '5g_penetration': 0.88},
        {'city': 'Miami', 'country': 'USA', 'continent': 'North America', 'region': 'Southeast', 'download_base': 220, 'upload_base': 38, 'latency_base': 16, '5g_penetration': 0.78},
        {'city': 'Seattle', 'country': 'USA', 'continent': 'North America', 'region': 'West', 'download_base': 235, 'upload_base': 41, 'latency_base': 13, '5g_penetration': 0.83},
        {'city': 'Boston', 'country': 'USA', 'continent': 'North America', 'region': 'Northeast', 'download_base': 245, 'upload_base': 43, 'latency_base': 11, '5g_penetration': 0.84},
        {'city': 'Austin', 'country': 'USA', 'continent': 'North America', 'region': 'South', 'download_base': 225, 'upload_base': 39, 'latency_base': 15, '5g_penetration': 0.79},
        {'city': 'Denver', 'country': 'USA', 'continent': 'North America', 'region': 'West', 'download_base': 210, 'upload_base': 36, 'latency_base': 18, '5g_penetration': 0.75},
        {'city': 'Toronto', 'country': 'Canada', 'continent': 'North America', 'region': 'East', 'download_base': 200, 'upload_base': 35, 'latency_base': 14, '5g_penetration': 0.80},
        {'city': 'Vancouver', 'country': 'Canada', 'continent': 'North America', 'region': 'West', 'download_base': 195, 'upload_base': 34, 'latency_base': 16, '5g_penetration': 0.78},
        {'city': 'Montreal', 'country': 'Canada', 'continent': 'North America', 'region': 'East', 'download_base': 190, 'upload_base': 33, 'latency_base': 15, '5g_penetration': 0.77},
        {'city': 'Mexico City', 'country': 'Mexico', 'continent': 'North America', 'region': 'Central', 'download_base': 120, 'upload_base': 25, 'latency_base': 28, '5g_penetration': 0.45},
        
        # Europe - Advanced 5G deployment
        {'city': 'London', 'country': 'UK', 'continent': 'Europe', 'region': 'Western', 'download_base': 180, 'upload_base': 40, 'latency_base': 18, '5g_penetration': 0.75},
        {'city': 'Berlin', 'country': 'Germany', 'continent': 'Europe', 'region': 'Western', 'download_base': 190, 'upload_base': 42, 'latency_base': 16, '5g_penetration': 0.78},
        {'city': 'Paris', 'country': 'France', 'continent': 'Europe', 'region': 'Western', 'download_base': 185, 'upload_base': 38, 'latency_base': 17, '5g_penetration': 0.76},
        {'city': 'Madrid', 'country': 'Spain', 'continent': 'Europe', 'region': 'Southern', 'download_base': 170, 'upload_base': 35, 'latency_base': 20, '5g_penetration': 0.65},
        {'city': 'Rome', 'country': 'Italy', 'continent': 'Europe', 'region': 'Southern', 'download_base': 165, 'upload_base': 32, 'latency_base': 22, '5g_penetration': 0.60},
        {'city': 'Amsterdam', 'country': 'Netherlands', 'continent': 'Europe', 'region': 'Western', 'download_base': 195, 'upload_base': 45, 'latency_base': 14, '5g_penetration': 0.82},
        {'city': 'Stockholm', 'country': 'Sweden', 'continent': 'Europe', 'region': 'Northern', 'download_base': 200, 'upload_base': 46, 'latency_base': 13, '5g_penetration': 0.85},
        {'city': 'Warsaw', 'country': 'Poland', 'continent': 'Europe', 'region': 'Eastern', 'download_base': 140, 'upload_base': 28, 'latency_base': 25, '5g_penetration': 0.50},
        {'city': 'Zurich', 'country': 'Switzerland', 'continent': 'Europe', 'region': 'Western', 'download_base': 210, 'upload_base': 48, 'latency_base': 12, '5g_penetration': 0.83},
        {'city': 'Oslo', 'country': 'Norway', 'continent': 'Europe', 'region': 'Northern', 'download_base': 195, 'upload_base': 44, 'latency_base': 15, '5g_penetration': 0.80},
        {'city': 'Copenhagen', 'country': 'Denmark', 'continent': 'Europe', 'region': 'Northern', 'download_base': 188, 'upload_base': 41, 'latency_base': 16, '5g_penetration': 0.78},
        {'city': 'Brussels', 'country': 'Belgium', 'continent': 'Europe', 'region': 'Western', 'download_base': 175, 'upload_base': 37, 'latency_base': 18, '5g_penetration': 0.70},
        {'city': 'Vienna', 'country': 'Austria', 'continent': 'Europe', 'region': 'Western', 'download_base': 180, 'upload_base': 39, 'latency_base': 17, '5g_penetration': 0.72},
        {'city': 'Dublin', 'country': 'Ireland', 'continent': 'Europe', 'region': 'Western', 'download_base': 170, 'upload_base': 36, 'latency_base': 19, '5g_penetration': 0.68},
        {'city': 'Prague', 'country': 'Czech Republic', 'continent': 'Europe', 'region': 'Eastern', 'download_base': 155, 'upload_base': 32, 'latency_base': 21, '5g_penetration': 0.55},
        {'city': 'Budapest', 'country': 'Hungary', 'continent': 'Europe', 'region': 'Eastern', 'download_base': 145, 'upload_base': 30, 'latency_base': 23, '5g_penetration': 0.48},
        {'city': 'Lisbon', 'country': 'Portugal', 'continent': 'Europe', 'region': 'Southern', 'download_base': 160, 'upload_base': 34, 'latency_base': 20, '5g_penetration': 0.58},
        {'city': 'Athens', 'country': 'Greece', 'continent': 'Europe', 'region': 'Southern', 'download_base': 135, 'upload_base': 28, 'latency_base': 26, '5g_penetration': 0.42},
        {'city': 'Helsinki', 'country': 'Finland', 'continent': 'Europe', 'region': 'Northern', 'download_base': 205, 'upload_base': 47, 'latency_base': 14, '5g_penetration': 0.84},
        
        # Asia - Mixed but rapidly advancing
        {'city': 'Tokyo', 'country': 'Japan', 'continent': 'Asia', 'region': 'East', 'download_base': 300, 'upload_base': 60, 'latency_base': 8, '5g_penetration': 0.90},
        {'city': 'Seoul', 'country': 'South Korea', 'continent': 'Asia', 'region': 'East', 'download_base': 320, 'upload_base': 65, 'latency_base': 7, '5g_penetration': 0.92},
        {'city': 'Singapore', 'country': 'Singapore', 'continent': 'Asia', 'region': 'Southeast', 'download_base': 280, 'upload_base': 55, 'latency_base': 10, '5g_penetration': 0.88},
        {'city': 'Hong Kong', 'country': 'China', 'continent': 'Asia', 'region': 'East', 'download_base': 270, 'upload_base': 52, 'latency_base': 11, '5g_penetration': 0.85},
        {'city': 'Shanghai', 'country': 'China', 'continent': 'Asia', 'region': 'East', 'download_base': 250, 'upload_base': 48, 'latency_base': 12, '5g_penetration': 0.82},
        {'city': 'Beijing', 'country': 'China', 'continent': 'Asia', 'region': 'East', 'download_base': 240, 'upload_base': 46, 'latency_base': 13, '5g_penetration': 0.80},
        {'city': 'Shenzhen', 'country': 'China', 'continent': 'Asia', 'region': 'East', 'download_base': 260, 'upload_base': 50, 'latency_base': 11, '5g_penetration': 0.83},
        {'city': 'Guangzhou', 'country': 'China', 'continent': 'Asia', 'region': 'East', 'download_base': 230, 'upload_base': 44, 'latency_base': 14, '5g_penetration': 0.78},
        {'city': 'Mumbai', 'country': 'India', 'continent': 'Asia', 'region': 'South', 'download_base': 150, 'upload_base': 30, 'latency_base': 22, '5g_penetration': 0.35},
        {'city': 'Delhi', 'country': 'India', 'continent': 'Asia', 'region': 'South', 'download_base': 145, 'upload_base': 28, 'latency_base': 24, '5g_penetration': 0.32},
        {'city': 'Bangalore', 'country': 'India', 'continent': 'Asia', 'region': 'South', 'download_base': 160, 'upload_base': 32, 'latency_base': 20, '5g_penetration': 0.40},
        {'city': 'Chennai', 'country': 'India', 'continent': 'Asia', 'region': 'South', 'download_base': 140, 'upload_base': 26, 'latency_base': 25, '5g_penetration': 0.30},
        {'city': 'Kolkata', 'country': 'India', 'continent': 'Asia', 'region': 'South', 'download_base': 130, 'upload_base': 24, 'latency_base': 27, '5g_penetration': 0.28},
        {'city': 'Hyderabad', 'country': 'India', 'continent': 'Asia', 'region': 'South', 'download_base': 155, 'upload_base': 31, 'latency_base': 21, '5g_penetration': 0.38},
        {'city': 'Bangkok', 'country': 'Thailand', 'continent': 'Asia', 'region': 'Southeast', 'download_base': 120, 'upload_base': 25, 'latency_base': 28, '5g_penetration': 0.25},
        {'city': 'Kuala Lumpur', 'country': 'Malaysia', 'continent': 'Asia', 'region': 'Southeast', 'download_base': 135, 'upload_base': 28, 'latency_base': 26, '5g_penetration': 0.30},
        {'city': 'Manila', 'country': 'Philippines', 'continent': 'Asia', 'region': 'Southeast', 'download_base': 100, 'upload_base': 20, 'latency_base': 32, '5g_penetration': 0.20},
        {'city': 'Jakarta', 'country': 'Indonesia', 'continent': 'Asia', 'region': 'Southeast', 'download_base': 95, 'upload_base': 18, 'latency_base': 35, '5g_penetration': 0.18},
        {'city': 'Hanoi', 'country': 'Vietnam', 'continent': 'Asia', 'region': 'Southeast', 'download_base': 110, 'upload_base': 22, 'latency_base': 30, '5g_penetration': 0.22},
        {'city': 'Ho Chi Minh City', 'country': 'Vietnam', 'continent': 'Asia', 'region': 'Southeast', 'download_base': 115, 'upload_base': 24, 'latency_base': 28, '5g_penetration': 0.25},
        {'city': 'Taipei', 'country': 'Taiwan', 'continent': 'Asia', 'region': 'East', 'download_base': 220, 'upload_base': 45, 'latency_base': 15, '5g_penetration': 0.75},
        {'city': 'Dubai', 'country': 'UAE', 'continent': 'Asia', 'region': 'Middle East', 'download_base': 200, 'upload_base': 42, 'latency_base': 16, '5g_penetration': 0.70},
        {'city': 'Riyadh', 'country': 'Saudi Arabia', 'continent': 'Asia', 'region': 'Middle East', 'download_base': 180, 'upload_base': 38, 'latency_base': 18, '5g_penetration': 0.60},
        {'city': 'Tel Aviv', 'country': 'Israel', 'continent': 'Asia', 'region': 'Middle East', 'download_base': 190, 'upload_base': 40, 'latency_base': 17, '5g_penetration': 0.65},
        {'city': 'Istanbul', 'country': 'Turkey', 'continent': 'Asia', 'region': 'Middle East', 'download_base': 125, 'upload_base': 26, 'latency_base': 24, '5g_penetration': 0.35},
        {'city': 'Tehran', 'country': 'Iran', 'continent': 'Asia', 'region': 'Middle East', 'download_base': 80, 'upload_base': 15, 'latency_base': 40, '5g_penetration': 0.15},
        {'city': 'Karachi', 'country': 'Pakistan', 'continent': 'Asia', 'region': 'South', 'download_base': 70, 'upload_base': 12, 'latency_base': 45, '5g_penetration': 0.10},
        {'city': 'Dhaka', 'country': 'Bangladesh', 'continent': 'Asia', 'region': 'South', 'download_base': 65, 'upload_base': 10, 'latency_base': 48, '5g_penetration': 0.08},
        {'city': 'Colombo', 'country': 'Sri Lanka', 'continent': 'Asia', 'region': 'South', 'download_base': 90, 'upload_base': 18, 'latency_base': 35, '5g_penetration': 0.20},
        {'city': 'Kathmandu', 'country': 'Nepal', 'continent': 'Asia', 'region': 'South', 'download_base': 60, 'upload_base': 8, 'latency_base': 50, '5g_penetration': 0.05},
        
        # South America - Developing but improving
        {'city': 'São Paulo', 'country': 'Brazil', 'continent': 'South America', 'region': 'East', 'download_base': 100, 'upload_base': 22, 'latency_base': 30, '5g_penetration': 0.25},
        {'city': 'Rio de Janeiro', 'country': 'Brazil', 'continent': 'South America', 'region': 'East', 'download_base': 95, 'upload_base': 20, 'latency_base': 32, '5g_penetration': 0.22},
        {'city': 'Buenos Aires', 'country': 'Argentina', 'continent': 'South America', 'region': 'South', 'download_base': 110, 'upload_base': 25, 'latency_base': 28, '5g_penetration': 0.30},
        {'city': 'Lima', 'country': 'Peru', 'continent': 'South America', 'region': 'West', 'download_base': 85, 'upload_base': 18, 'latency_base': 35, '5g_penetration': 0.18},
        {'city': 'Bogotá', 'country': 'Colombia', 'continent': 'South America', 'region': 'North', 'download_base': 90, 'upload_base': 19, 'latency_base': 33, '5g_penetration': 0.20},
        {'city': 'Santiago', 'country': 'Chile', 'continent': 'South America', 'region': 'South', 'download_base': 120, 'upload_base': 28, 'latency_base': 25, '5g_penetration': 0.35},
        {'city': 'Caracas', 'country': 'Venezuela', 'continent': 'South America', 'region': 'North', 'download_base': 50, 'upload_base': 8, 'latency_base': 55, '5g_penetration': 0.05},
        {'city': 'Quito', 'country': 'Ecuador', 'continent': 'South America', 'region': 'West', 'download_base': 75, 'upload_base': 15, 'latency_base': 38, '5g_penetration': 0.15},
        {'city': 'Montevideo', 'country': 'Uruguay', 'continent': 'South America', 'region': 'South', 'download_base': 130, 'upload_base': 30, 'latency_base': 22, '5g_penetration': 0.40},
        {'city': 'La Paz', 'country': 'Bolivia', 'continent': 'South America', 'region': 'West', 'download_base': 60, 'upload_base': 10, 'latency_base': 45, '5g_penetration': 0.08},
        
        # Africa - Emerging markets
        {'city': 'Cairo', 'country': 'Egypt', 'continent': 'Africa', 'region': 'North', 'download_base': 80, 'upload_base': 16, 'latency_base': 38, '5g_penetration': 0.20},
        {'city': 'Lagos', 'country': 'Nigeria', 'continent': 'Africa', 'region': 'West', 'download_base': 70, 'upload_base': 14, 'latency_base': 42, '5g_penetration': 0.15},
        {'city': 'Nairobi', 'country': 'Kenya', 'continent': 'Africa', 'region': 'East', 'download_base': 85, 'upload_base': 18, 'latency_base': 35, '5g_penetration': 0.25},
        {'city': 'Johannesburg', 'country': 'South Africa', 'continent': 'Africa', 'region': 'South', 'download_base': 95, 'upload_base': 20, 'latency_base': 32, '5g_penetration': 0.30},
        {'city': 'Casablanca', 'country': 'Morocco', 'continent': 'Africa', 'region': 'North', 'download_base': 88, 'upload_base': 17, 'latency_base': 36, '5g_penetration': 0.22},
        {'city': 'Accra', 'country': 'Ghana', 'continent': 'Africa', 'region': 'West', 'download_base': 75, 'upload_base': 15, 'latency_base': 40, '5g_penetration': 0.18},
        {'city': 'Addis Ababa', 'country': 'Ethiopia', 'continent': 'Africa', 'region': 'East', 'download_base': 55, 'upload_base': 10, 'latency_base': 48, '5g_penetration': 0.08},
        {'city': 'Kampala', 'country': 'Uganda', 'continent': 'Africa', 'region': 'East', 'download_base': 65, 'upload_base': 12, 'latency_base': 44, '5g_penetration': 0.12},
        {'city': 'Dar es Salaam', 'country': 'Tanzania', 'continent': 'Africa', 'region': 'East', 'download_base': 72, 'upload_base': 14, 'latency_base': 41, '5g_penetration': 0.15},
        {'city': 'Abidjan', 'country': 'Ivory Coast', 'continent': 'Africa', 'region': 'West', 'download_base': 78, 'upload_base': 16, 'latency_base': 39, '5g_penetration': 0.20},
        {'city': 'Algiers', 'country': 'Algeria', 'continent': 'Africa', 'region': 'North', 'download_base': 82, 'upload_base': 17, 'latency_base': 37, '5g_penetration': 0.21},
        {'city': 'Khartoum', 'country': 'Sudan', 'continent': 'Africa', 'region': 'North', 'download_base': 45, 'upload_base': 8, 'latency_base': 52, '5g_penetration': 0.05},
        {'city': 'Luanda', 'country': 'Angola', 'continent': 'Africa', 'region': 'Central', 'download_base': 68, 'upload_base': 13, 'latency_base': 43, '5g_penetration': 0.10},
        {'city': 'Dakar', 'country': 'Senegal', 'continent': 'Africa', 'region': 'West', 'download_base': 80, 'upload_base': 16, 'latency_base': 38, '5g_penetration': 0.18},
        {'city': 'Harare', 'country': 'Zimbabwe', 'continent': 'Africa', 'region': 'South', 'download_base': 58, 'upload_base': 11, 'latency_base': 46, '5g_penetration': 0.07},
        
        # Oceania
        {'city': 'Sydney', 'country': 'Australia', 'continent': 'Oceania', 'region': 'East', 'download_base': 150, 'upload_base': 35, 'latency_base': 20, '5g_penetration': 0.65},
        {'city': 'Melbourne', 'country': 'Australia', 'continent': 'Oceania', 'region': 'South', 'download_base': 145, 'upload_base': 33, 'latency_base': 22, '5g_penetration': 0.62},
        {'city': 'Auckland', 'country': 'New Zealand', 'continent': 'Oceania', 'region': 'North', 'download_base': 140, 'upload_base': 32, 'latency_base': 24, '5g_penetration': 0.58},
        {'city': 'Brisbane', 'country': 'Australia', 'continent': 'Oceania', 'region': 'East', 'download_base': 135, 'upload_base': 30, 'latency_base': 25, '5g_penetration': 0.55},
        {'city': 'Perth', 'country': 'Australia', 'continent': 'Oceania', 'region': 'West', 'download_base': 125, 'upload_base': 28, 'latency_base': 28, '5g_penetration': 0.48},
        {'city': 'Wellington', 'country': 'New Zealand', 'continent': 'Oceania', 'region': 'South', 'download_base': 130, 'upload_base': 29, 'latency_base': 26, '5g_penetration': 0.52},
        {'city': 'Adelaide', 'country': 'Australia', 'continent': 'Oceania', 'region': 'South', 'download_base': 128, 'upload_base': 28, 'latency_base': 27, '5g_penetration': 0.50},
        {'city': 'Christchurch', 'country': 'New Zealand', 'continent': 'Oceania', 'region': 'South', 'download_base': 122, 'upload_base': 27, 'latency_base': 29, '5g_penetration': 0.45},
        {'city': 'Honolulu', 'country': 'USA', 'continent': 'Oceania', 'region': 'Central', 'download_base': 160, 'upload_base': 36, 'latency_base': 18, '5g_penetration': 0.70},
        {'city': 'Port Moresby', 'country': 'Papua New Guinea', 'continent': 'Oceania', 'region': 'Melanesia', 'download_base': 40, 'upload_base': 6, 'latency_base': 60, '5g_penetration': 0.02},
        {'city': 'Suva', 'country': 'Fiji', 'continent': 'Oceania', 'region': 'Melanesia', 'download_base': 55, 'upload_base': 9, 'latency_base': 50, '5g_penetration': 0.05},
    ]
    
    # Modern device list (2023-2024 models)
    modern_devices = [
        # Flagship 2024
        'iPhone 15 Pro Max', 'iPhone 15 Pro', 'iPhone 15', 'iPhone 15 Plus',
        'Samsung Galaxy S24 Ultra', 'Samsung Galaxy S24+', 'Samsung Galaxy S24',
        'Google Pixel 8 Pro', 'Google Pixel 8',
        
        # Flagship 2023
        'iPhone 14 Pro Max', 'iPhone 14 Pro', 'iPhone 14', 'iPhone 14 Plus',
        'Samsung Galaxy S23 Ultra', 'Samsung Galaxy S23+', 'Samsung Galaxy S23',
        'Google Pixel 7 Pro', 'Google Pixel 7', 'Google Pixel 7a',
        
        # Foldables 2023-2024
        'Samsung Galaxy Z Fold5', 'Samsung Galaxy Z Flip5',
        'Google Pixel Fold', 'OnePlus Open',
        
        # Mid-range 2023-2024
        'Samsung Galaxy A54', 'Samsung Galaxy A34', 'Samsung Galaxy A15',
        'Google Pixel 6a', 'OnePlus Nord 3', 'OnePlus Nord CE 3',
        'Xiaomi 13T', 'Xiaomi 13T Pro', 'Xiaomi Redmi Note 13 Pro+',
        
        # Budget 2023-2024
        'Samsung Galaxy A14', 'Samsung Galaxy A05s',
        'Xiaomi Redmi 12', 'Xiaomi Redmi Note 12',
        'Realme 11', 'Realme Narzo 60',
        'Motorola Moto G54', 'Motorola Moto G34',
        
        # Regional popular devices
        'Vivo V29', 'Vivo V29e', 'Oppo Reno 11', 'Oppo A78',
        'Tecno Camon 20', 'Tecno Spark 10 Pro', 'Infinix Hot 30',
        'Huawei P60', 'Huawei Nova 11',
        
        # Older but still widely used
        'iPhone 13 Pro', 'iPhone 13', 'iPhone 12',
        'Samsung Galaxy S21 FE', 'Samsung Galaxy A53',
        'Google Pixel 6', 'OnePlus 11R',
        
        # Tablets with cellular
        'iPad Pro 12.9" (2024)', 'iPad Pro 11" (2024)', 'iPad Air (2024)',
        'Samsung Galaxy Tab S9', 'Samsung Galaxy Tab S9 FE',
    ]
    
    # Modern network types with realistic 2024 distribution
    network_types = ['5G NSA', '5G SA', '4G LTE-A', '4G LTE', '4G', '3G']
    # Probabilities vary by location 5G penetration
    
    # Modern 5G bands (mmWave and Sub-6)
    modern_bands = [
        # mmWave bands (high speed, short range)
        'n257', 'n258', 'n259', 'n260', 'n261',
        # Sub-6 GHz bands (balance of speed and coverage)
        'n1', 'n3', 'n5', 'n7', 'n8', 'n20', 'n28', 'n38', 'n41', 'n48',
        'n66', 'n71', 'n77', 'n78', 'n79', 'n90', 'n96', 'n100', 'n101',
        # 4G bands still in use
        'B1', 'B3', 'B7', 'B8', 'B20', 'B28', 'B32', 'B38', 'B40', 'B41', 'B42'
    ]
    
    carriers_by_region = {
        'North America': ['Verizon', 'AT&T', 'T-Mobile', 'Rogers', 'Telus', 'Bell', 'Telcel', 'Movistar'],
        'Europe': ['Vodafone', 'Deutsche Telekom', 'Orange', 'Telefónica', 'BT', 'EE', 'Three', 'O2'],
        'Asia': ['NTT Docomo', 'SK Telecom', 'KT', 'LG U+', 'Singtel', 'StarHub', 'Airtel', 'Jio', 'China Mobile'],
        'South America': ['Claro', 'Movistar', 'TIM', 'Vivo', 'Entel', 'Personal'],
        'Africa': ['MTN', 'Vodacom', 'Orange', 'Airtel Africa', 'Safaricom'],
        'Oceania': ['Telstra', 'Optus', 'Spark', 'Vodafone NZ']
    }
    
    data = []
    
    for i in range(num_records):
        # Randomly select a location
        loc = np.random.choice(global_locations)
        continent = loc['continent']
        five_g_penetration = loc['5g_penetration']
        
        # Dynamic network type probabilities based on 5G penetration
        if five_g_penetration > 0.7:  # High 5G areas
            network_probs = [0.35, 0.25, 0.20, 0.15, 0.04, 0.01]
        elif five_g_penetration > 0.4:  # Medium 5G areas
            network_probs = [0.25, 0.15, 0.25, 0.20, 0.10, 0.05]
        else:  # Low 5G areas
            network_probs = [0.10, 0.05, 0.30, 0.35, 0.15, 0.05]
        
        network_type = np.random.choice(network_types, p=network_probs)
        
        # Get region-appropriate carriers
        carriers = carriers_by_region.get(continent, ['Generic Carrier'])
        carrier = np.random.choice(carriers)
        
        # Base performance with modern realistic speeds
        base_download = loc['download_base']
        base_upload = loc['upload_base']
        base_latency = loc['latency_base']
        
        # Network type performance multipliers (2024 realistic)
        network_multipliers = {
            '5G SA': (1.2, 1.1, 0.8),   # (download, upload, latency)
            '5G NSA': (1.1, 1.0, 0.9),
            '4G LTE-A': (0.8, 0.7, 1.0),
            '4G LTE': (0.6, 0.5, 1.2),
            '4G': (0.4, 0.3, 1.5),
            '3G': (0.1, 0.08, 2.0)
        }
        
        mult_dl, mult_ul, mult_lat = network_multipliers[network_type]
        
        # More natural performance variations using log-normal distributions
        # This creates realistic right-skewed distributions common in network speeds
        download_speed = max(1, np.random.lognormal(np.log(base_download * mult_dl), 0.4))
        upload_speed = max(0.5, np.random.lognormal(np.log(base_upload * mult_ul), 0.5))
        latency = max(5, np.random.lognormal(np.log(base_latency * mult_lat), 0.3))
        
        # Signal strength affects performance naturally
        signal_strength = np.random.normal(-75, 15)
        signal_factor = max(0.1, min(1.5, (signal_strength + 100) / 50))  # -50dBm = 1.0, -100dBm = 0.0
        
        download_speed *= signal_factor
        upload_speed *= signal_factor
        latency /= signal_factor
        
        # Time-based variations (rush hour, night, etc.)
        current_hour = np.random.randint(0, 24)
        if 7 <= current_hour <= 9 or 17 <= current_hour <= 19:  # Rush hours
            download_speed *= np.random.uniform(0.5, 0.8)
            upload_speed *= np.random.uniform(0.4, 0.7)
            latency *= np.random.uniform(1.2, 1.8)
        elif 0 <= current_hour <= 5:  # Night hours
            download_speed *= np.random.uniform(1.1, 1.4)
            upload_speed *= np.random.uniform(1.0, 1.3)
            latency *= np.random.uniform(0.8, 0.95)
        
        # More realistic jitter based on latency and network type
        base_jitter = latency * np.random.uniform(0.05, 0.15)  # Jitter is 5-15% of latency
        jitter = max(0.1, np.random.exponential(base_jitter))
        
        # Device capability variations (flagship vs budget)
        device = np.random.choice(modern_devices)
        if 'Pro' in device or 'Ultra' in device or 'Fold' in device:
            # Flagship devices have better modems
            download_speed *= np.random.uniform(1.05, 1.15)
            upload_speed *= np.random.uniform(1.05, 1.12)
            latency *= np.random.uniform(0.92, 0.98)
        elif 'A' in device or 'Redmi' in device or 'Moto G' in device:
            # Budget devices have more modest performance
            download_speed *= np.random.uniform(0.85, 0.95)
            upload_speed *= np.random.uniform(0.82, 0.92)
            latency *= np.random.uniform(1.05, 1.15)
        
        record = {
            'Timestamp': datetime.now() - timedelta(hours=np.random.randint(0, 8760)),  # Up to 1 year
            'Location': loc['city'],
            'Country': loc['country'],
            'Continent': continent,
            'Region': loc['region'],
            'Signal_Strength_dBm': signal_strength,
            'Download_Speed_Mbps': max(0.1, download_speed),
            'Upload_Speed_Mbps': max(0.1, upload_speed),
            'Latency_ms': max(2, latency),
            'Jitter_ms': max(0.1, jitter),
            'Network_Type': network_type,
            'Device_Model': device,
            'Carrier': carrier,
            'Band': np.random.choice(modern_bands),
            'Battery_Level_%': np.random.randint(15, 100),
            'Temperature_C': np.random.normal(30, 6),
            'Connected_Duration_min': np.random.exponential(60),
            'Handover_Count': np.random.poisson(2),
            'Data_Usage_MB': np.random.exponential(500),
            'Video_Streaming_Quality': np.random.randint(2, 6),
            'VoNR_Enabled': np.random.choice([True, False], p=[0.5, 0.5]),
            'Network_Congestion_Level': np.random.choice(['Low', 'Medium', 'High'], p=[0.5, 0.35, 0.15]),
            'Ping_to_Google_ms': max(8, latency + np.random.exponential(3)),
            'Dropped_Connection': np.random.choice([True, False], p=[0.03, 0.97])
        }
        data.append(record)
    
    return pd.DataFrame(data)

# Generate the modern global dataset
print("🌍 Generating modern global network performance dataset...")
df_modern = create_modern_global_network_dataset(30000)

# Save to CSV
df_modern.to_csv('modern_global_network_data.csv', index=False)

print("✅ Modern global dataset created: 'modern_global_network_data.csv'")
print(f"📊 Total records: {len(df_modern)}")
print(f"🏙️ Cities covered: {df_modern['Location'].nunique()}")
print(f"🌐 Countries covered: {df_modern['Country'].nunique()}")
print(f"🗺️ Continents covered: {df_modern['Continent'].unique()}")
print(f"📱 Device models: {df_modern['Device_Model'].nunique()}")
print(f"📶 Network types: {df_modern['Network_Type'].unique()}")
print(f"🏢 Carriers: {df_modern['Carrier'].nunique()}")
print(f"📡 Frequency bands: {df_modern['Band'].nunique()}")
print(f"📥 Average Download Speed: {df_modern['Download_Speed_Mbps'].mean():.1f} Mbps")
print(f"📤 Average Upload Speed: {df_modern['Upload_Speed_Mbps'].mean():.1f} Mbps")
print(f"⏱️ Average Latency: {df_modern['Latency_ms'].mean():.1f} ms")
print(f"📊 5G Penetration: {(df_modern['Network_Type'].str.contains('5G').sum() / len(df_modern) * 100):.1f}%")