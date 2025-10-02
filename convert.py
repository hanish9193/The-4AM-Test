import pandas as pd
import os
import numpy as np

# Create the master dataset for the 4 AM Test
print("🚀 Starting 4 AM Test Data Merge...")

# Function to clean and merge batch files
def merge_batches(search_term, num_batches=4):
    """
    Merge multiple Google Trends batch files into one clean dataset
    """
    all_data = []
    
    for batch_num in range(1, num_batches + 1):
        filename = f"{search_term.upper()}_BATCH{batch_num}.csv"
        
        if os.path.exists(filename):
            print(f"📊 Processing {filename}...")
            
            # Read the CSV file
            df = pd.read_csv(filename, skiprows=2)  # Skip the header rows
            
            # Get the column names (first row has the countries/search terms)
            columns = df.columns.tolist()
            
            # Create a dictionary to store country data
            country_data = {}
            
            # Process each column (skip the first 'Week' column)
            for i, col in enumerate(columns[1:], 1):
                # Extract country name (remove the search term part)
                country_name = col.split(':')[0].strip()
                
                # Calculate average search interest for this country
                country_avg = df[col].replace('<1', 0.5).astype(float).mean()
                country_data[country_name] = round(country_avg, 1)
            
            all_data.append(country_data)
        else:
            print(f"⚠️  Warning: {filename} not found")
    
    # Combine all batches
    combined_data = {}
    for batch_data in all_data:
        combined_data.update(batch_data)
    
    # Convert to DataFrame
    result_df = pd.DataFrame(list(combined_data.items()), 
                           columns=['Country', f'{search_term}_Score'])
    
    # Remove any duplicate countries (keep first occurrence)
    result_df = result_df.drop_duplicates(subset=['Country'], keep='first')
    
    # Sort by score (descending)
    result_df = result_df.sort_values(f'{search_term}_Score', ascending=False)
    
    return result_df

# Merge each search term
print("\n1️⃣ Merging ANXIETY batches...")
anxiety_df = merge_batches('anxiety')
print(f"   ✅ Found {len(anxiety_df)} countries with anxiety data")

print("\n2️⃣ Merging CAN'T SLEEP batches...")
sleep_df = merge_batches('cant_sleep')
print(f"   ✅ Found {len(sleep_df)} countries with sleep data")

print("\n3️⃣ Merging DEPRESSION batches...")
depression_df = merge_batches('depression')
print(f"   ✅ Found {len(depression_df)} countries with depression data")

# Combine all three datasets
print("\n4️⃣ Combining all mental health indicators...")
final_df = anxiety_df.merge(sleep_df, on='Country', how='outer')
final_df = final_df.merge(depression_df, on='Country', how='outer')

# Fill missing values with 0 (some countries might not have all indicators)
final_df = final_df.fillna(0)

# Create a combined "Distress Score" (average of all three)
final_df['Distress_Score'] = (
    final_df['anxiety_Score'] + 
    final_df['cant_sleep_Score'] + 
    final_df['depression_Score']
) / 3

# Round to 1 decimal place
final_df['Distress_Score'] = final_df['Distress_Score'].round(1)

# Sort by distress score
final_df = final_df.sort_values('Distress_Score', ascending=False)

# Add some sample "Official Happiness" data (we'll replace this with real OECD data)
# This is just placeholder data for now
sample_happiness = {
    'Finland': 7.8, 'Denmark': 7.6, 'Sweden': 7.4, 'Norway': 7.3,
    'Netherlands': 7.2, 'Switzerland': 7.1, 'Germany': 6.9,
    'United Kingdom': 6.8, 'United States': 6.7, 'France': 6.6,
    'Canada': 6.5, 'Australia': 6.4, 'Japan': 5.9, 'South Korea': 5.7,
    'Italy': 6.0, 'Spain': 6.3, 'Belgium': 6.8, 'Austria': 7.0,
    'Brazil': 6.1, 'Mexico': 6.2, 'India': 4.9
}

# Add happiness scores where available
final_df['Official_Happiness'] = final_df['Country'].map(sample_happiness)

# Calculate "The Gap" (Official Happiness - Reality/Distress)
# Higher gap = more difference between what they claim vs reality
final_df['The_Gap'] = final_df['Official_Happiness'] - (final_df['Distress_Score'] / 10)

# Clean up the dataset
final_df = final_df.dropna(subset=['Official_Happiness'])  # Only keep countries with happiness data
final_df = final_df.round(2)

# Save all the files
print("\n5️⃣ Saving files...")

# Individual search term files
anxiety_df.to_csv('anxiety_final.csv', index=False)
sleep_df.to_csv('cant_sleep_final.csv', index=False)
depression_df.to_csv('depression_final.csv', index=False)

# Master file for Plotly
final_df.to_csv('4am_test_master.csv', index=False)

print("✅ Files saved:")
print("   📄 anxiety_final.csv")
print("   📄 cant_sleep_final.csv") 
print("   📄 depression_final.csv")
print("   📄 4am_test_master.csv")

print(f"\n🎯 MASTER DATASET PREVIEW:")
print(f"📊 {len(final_df)} countries with complete data")
print("\nTop 5 countries by 'The Gap' (biggest difference between official happiness and reality):")
print(final_df.nlargest(5, 'The_Gap')[['Country', 'Official_Happiness', 'Distress_Score', 'The_Gap']])

print(f"\n🌙 TOP DISTRESS COUNTRIES (4 AM searches):")
print(final_df.nlargest(5, 'Distress_Score')[['Country', 'Distress_Score']])

print(f"\n😊 OFFICIAL HAPPINESS LEADERS:")
print(final_df.nlargest(5, 'Official_Happiness')[['Country', 'Official_Happiness']])

print("\n🚀 READY FOR PLOTLY STUDIO!")
print("📁 Upload '4am_test_master.csv' to create your winning visualization!")