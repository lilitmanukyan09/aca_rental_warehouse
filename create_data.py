#importing libraries
import numpy as np
import pandas as pd
from faker import Faker
from collections import defaultdict
import random
import warnings
warnings.filterwarnings("ignore")
import datetime



properties = pd.read_csv('properties.csv', index_col = 0)
properties = properties.rename(columns = {'furnishing_state':'furnishing'})

building_features_list = ['Fitness area', 'On-site management', 'Secure Entry', 'Guest Parking', 'Party/Games Room', 'Concierge', 'Steam Room', 'Sauna']
property_features_list = ['Balcony', 'Air Conditioning', 'Dishwasher', 'Elevator', 'Oven/Stove', 'Laundry', 'Fridge', 'Microwave', 'Window Coverings', 'Hardwood Floors', 'City views', 'Storage Lockers']
community_features_list = ['Bike Paths', 'Bus', 'Ocean', 'Outdoor Pool', 'Playground/Park', 'Public Library', 'River', 'Shopping center', 'Tennis Courts', 'Golf Course', 'Lake']


#Creating tables for features

building_features = pd.DataFrame(building_features_list, columns = ['feature'])
building_features.insert(0, 'feature_id', range(1, 1+len(building_features)))

property_features = pd.DataFrame(property_features_list, columns = ['feature'])
property_features.insert(0, 'feature_id', range(1, 1+len(property_features)))

community_features = pd.DataFrame(community_features_list, columns = ['feature'])
community_features.insert(0, 'feature_id', range(1, 1+len(community_features)))

print('created features tables')

#splitting location into street and address
new = properties['location'].str.split(" ", n = 1, expand = True)
properties['building'] = new[0]
properties['street'] = new[1]
properties[['building', 'street']] = properties[['building', 'street']].replace({',':''}, regex = True)
properties[['building', 'street']] = properties[['building', 'street']].replace({'-':''}, regex = True)
properties['deposit'] = properties['deposit'].replace({',':''}, regex = True)
properties['size'] = properties['size'].replace({', ':''}, regex = True)
properties.drop(columns = ['location'], inplace = True )

#cleaning several columns
properties['deposit'] = properties['deposit'].str.replace('$', '')
properties['beds'] = properties['beds'].str.replace(' bd', '')
properties['baths'] = properties['baths'].str.replace(' ba', '')
properties['size'] = properties['size'].str.replace('ft2', '')

print('Cleaning and manipulation done!')

#creating dimension tables
region = pd.DataFrame(properties['region'].unique(), columns = ['region'])
region.insert(0, 'region_id', range(1, 1+len(region)))



city = pd.DataFrame(properties['city'].unique(), columns = ['city'])    
city.insert(0, 'city_id', range(1, 1+len(city)))

location = [properties['building'], properties['street']]
location = pd.concat(location, axis = 1, keys = ['building', 'street'])
location.insert(0, 'location_id', range(1, 1+len(location)))
location = pd.DataFrame(location)
location[['building', 'street']] = location[['building', 'street']].replace({',':''}, regex = True)
location[['building', 'street']] = location[['building', 'street']].replace({'-':''}, regex = True)


property_type = pd.DataFrame(properties['property_type'].unique(), columns = ['property_type'])
property_type.insert(0, 'property_type_id', range(1, 1+len(property_type)))


  
furnishing = pd.DataFrame(properties['furnishing'].unique(), columns = ['furnishing'])  
furnishing.insert(0, 'furnish_state_id', range(1, 1+len(furnishing)))


lease_term = pd.DataFrame(properties['lease_term'].unique(), columns = ['lease_term'])  
lease_term.insert(0, 'lease_term_id', range(1, 1+len(lease_term)))


availability = pd.DataFrame(properties['availability'].unique(), columns = ['availability'])    
availability.insert(0, 'availability_id', range(1, 1+len(availability)))



print('Creating dimension tables')

fake = Faker()

#creating users table
users = defaultdict(list)
for j in range(5000):
    users['user_id'].append(j)
    users["first_name"].append( fake.first_name() )
    users["last_name"].append( fake.last_name() )
    users["occupation"].append( fake.job() )
    users["birthdate"].append( fake.date_of_birth() )
    users["country"].append( fake.country() )
    users["created"].append( fake.date_time_this_decade())

users = pd.DataFrame(users)
users['occupation'] = users['occupation'].replace({',':''}, regex = True)


print('Created user table')

#creating logs table
logs = defaultdict(list)
for k in range (10000):
    # logs['log_id'].append(k)
    logs['user_id'].append(random.choices(users['user_id'], k = 1)[0])
    logs['property_id'].append(random.choices(properties['property_id'].unique(), k = 1)[0])
    logs['date'].append(fake.date_time_this_month())
logs = pd.DataFrame(logs)


print('Created log table')

#creating tenant table
tenants = defaultdict(list)

for i in range(400):
    tenants['tenant_id'].append(i)
    tenants['family_members'].append(random.sample(range(1, 8), 1)[0])
    tenants['full_name'].append(random.sample(list(users.first_name + " " + users.last_name), 1)[0])

tenants = pd.DataFrame(tenants)


print('Created tenants table')

# Creating transactions table
transactions = defaultdict(list)
for l in range (1000):
    # transactions['transaction_id'].append(l)
    transactions['tenant_id'].append(np.random.choice(tenants['tenant_id'].unique()))
    transactions['property_id'].append(np.random.choice(properties['property_id'].unique()))
    transactions['date'].append(fake.date_time_this_month())

transactions = pd.DataFrame(transactions)
transactions = transactions.drop_duplicates(subset=['property_id', 'tenant_id'], keep = 'last')

print('Created transactions table')


#Creating stay table 
stay = pd.DataFrame(transactions[['tenant_id', 'property_id', 'date']])
stay['start_date'] = (stay['date'] + datetime.timedelta(days=10)).dt.date
stay['end_date'] = stay['start_date'] + datetime.timedelta(days=3)
stay.drop('date', axis = 1, inplace = True)

print('Created stay table')


# Creating property_junction table
property_junction = defaultdict(list)
for _ in range (3000):
    property_junction['property_id'].append(np.random.choice(properties.property_id))
    property_junction['feature_id'].append(np.random.choice(property_features.feature_id))
   
property_junction = pd.DataFrame(property_junction)

# Creating building_junction table
building_junction = defaultdict(list)
for _ in range (500):
    building_junction['property_id'].append(np.random.choice(properties.property_id))
    building_junction['feature_id'].append(np.random.choice(building_features.feature_id))
   
building_junction = pd.DataFrame(building_junction)

# Creating community_junction table
community_junction = defaultdict(list)
for _ in range (500):
    community_junction['property_id'].append(np.random.choice(properties.property_id))
    community_junction['feature_id'].append(np.random.choice(community_features.feature_id))
   
community_junction = pd.DataFrame(community_junction)

print('Phew! Created junction tables as well!')

properties = properties.merge(region, how = 'left').drop('region', axis = 1)
properties = properties.merge(city, how = 'left').drop('city', axis = 1)
properties = properties.merge(property_type, how = 'left').drop('property_type', axis = 1)
properties = properties.merge(furnishing, how = 'left').drop('furnishing', axis = 1)
properties = properties.merge(lease_term, how = 'left').drop('lease_term', axis = 1)
properties = properties.merge(availability, how = 'left').drop('availability', axis = 1)
properties = properties.merge(location, how = 'left', left_on= ['building', 'street'], right_on=['building', 'street']).drop(['building', 'street'], axis = 1)
properties = properties.rename(columns = {'state_id':'furnish_state_id'})
properties.drop_duplicates(subset = ['property_id'], inplace=True)
