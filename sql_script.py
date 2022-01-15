import create_data

commands = (
        """ 
        DROP TABLE IF EXISTS 
            Region,
            City,
            Location,
            property_type,
            furnishing,
            lease_term,
            availability,
            property_features,
            building_features,
            community_features,
            tenants,
            properties,
            transactions,
            users,
            logs,
            stay,
            property_junction,
            building_junction,
            community_junction
        """,
        """
        CREATE TABLE IF NOT EXISTS Region (
            region_id INTEGER NOT NULL,
            region VARCHAR(255) NOT NULL,
            PRIMARY KEY (region_id)
        )
        """, 
        """
        CREATE TABLE IF NOT EXISTS City (
            city_id INTEGER,
            city VARCHAR(255) NOT NULL,
            PRIMARY KEY (city_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Location (
            location_id INTEGER,
            building VARCHAR(255),
            street VARCHAR(255),
            PRIMARY KEY (location_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS property_type (
            property_type_id INTEGER,
            property_type VARCHAR(255),
            PRIMARY KEY (property_type_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS furnishing (
            furnish_state_id INTEGER,
            furnishing VARCHAR(255),
            PRIMARY KEY (furnish_state_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS lease_term (
            lease_term_id INTEGER,
            lease_term VARCHAR(255),
            PRIMARY KEY (lease_term_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS availability (
            availability_id INTEGER,
            availability VARCHAR(255), 
            PRIMARY KEY (availability_id)
        )
        """,        
        """
        CREATE TABLE IF NOT EXISTS property_features (
            feature_id INTEGER,
            feature VARCHAR(255), 
            PRIMARY KEY (feature_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS building_features (
            feature_id INTEGER,
            feature VARCHAR(255),
            PRIMARY KEY (feature_id)
 
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS community_features (
            feature_id INTEGER,
            feature VARCHAR(255),
            PRIMARY KEY (feature_id)

        )
        """,
        """
        CREATE TABLE IF NOT EXISTS tenants (
            tenant_id INTEGER,
            family_members INT,
            full_name VARCHAR(255),
            PRIMARY KEY (tenant_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS properties (
            property_id INTEGER,
            region_id INTEGER,
            city_id INTEGER,
            location_id INTEGER,
            property_type_id INTEGER, 
            furnish_state_id INTEGER, 
            lease_term_id INTEGER, 
            availability_id INTEGER, 
            rent FLOAT,
            deposit VARCHAR(255),
            beds VARCHAR(255),
            baths VARCHAR(255),
            size VARCHAR(255),
            pets VARCHAR(255),
            smoking VARCHAR(255),
            parking VARCHAR(255),
            PRIMARY KEY (property_id),
            FOREIGN KEY (region_id) REFERENCES region (region_id),
            FOREIGN KEY (city_id) REFERENCES city (city_id),
            FOREIGN KEY (location_id) REFERENCES location (location_id),
            FOREIGN KEY (property_type_id) REFERENCES property_type (property_type_id),
            FOREIGN KEY (furnish_state_id) REFERENCES furnishing (furnish_state_id),
            FOREIGN KEY (lease_term_id) REFERENCES lease_term (lease_term_id),
            FOREIGN KEY (availability_id) REFERENCES availability (availability_id)
        )
        """,              
        """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id SERIAL,
            date TIMESTAMP,
            tenant_id INTEGER,
            property_id INTEGER, 
            PRIMARY KEY (transaction_id),
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (tenant_id) REFERENCES tenants (tenant_id)
        )
        """,   
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER,
            first_name VARCHAR,
            last_name VARCHAR(255),
            occupation VARCHAR(255),
            birthdate VARCHAR(255),
            country VARCHAR(255),
            created TIMESTAMP,
            PRIMARY KEY (user_id)
        )
        """,                 
        """
        CREATE TABLE IF NOT EXISTS logs (
            log_id SERIAL PRIMARY KEY,
            user_id INTEGER, 
            property_id INTEGER, 
            date TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (property_id) REFERENCES properties (property_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS stay (
            stay_id SERIAL PRIMARY KEY,
            tenant_id INTEGER,
            property_id INTEGER,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,            
            FOREIGN KEY (tenant_id) REFERENCES tenants (tenant_id),
            FOREIGN KEY (property_id) REFERENCES properties (property_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS property_junction (
            property_id INTEGER, 
            feature_id INTEGER,
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (feature_id) REFERENCES property_features (feature_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS building_junction (
            property_id INTEGER, 
            feature_id INTEGER,
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (feature_id) REFERENCES building_features (feature_id)
        )
        """, 
        """
        CREATE TABLE IF NOT EXISTS community_junction (
            property_id INTEGER, 
            feature_id INTEGER,
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (feature_id) REFERENCES community_features (feature_id)
        )
        """                        
        )

table_names = {
            'region' : create_data.region,        
            'city' : create_data.city,
            'location' : create_data.location,
            'property_type' : create_data.property_type,
            'furnishing' : create_data.furnishing,
            'lease_term' : create_data.lease_term,
            'availability' : create_data.availability,
            'property_features' : create_data.property_features,
            'building_features' : create_data.building_features,
            'community_features' : create_data.community_features,
            'tenants' : create_data.tenants,
            'properties' : create_data.properties,
            'transactions' : create_data.transactions,
            'users' : create_data.users,
            'logs' : create_data.logs,
            'stay' : create_data.stay,
            'property_junction' : create_data.property_junction,
            'building_junction' : create_data.building_junction,
            'community_junction' : create_data.community_junction,

}