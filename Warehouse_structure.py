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
            community_junction CASCADE;
        """,
        """
        CREATE TABLE IF NOT EXISTS Region (
            region_id BIGINT NOT NULL,
            region VARCHAR(255) NOT NULL,
            PRIMARY KEY (region_id)
        )
        """, 
        """
        CREATE TABLE IF NOT EXISTS City (
            city_id BIGINT,
            city VARCHAR(255) NOT NULL,
            PRIMARY KEY (city_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Location (
            location_id BIGINT,
            building VARCHAR(255),
            street VARCHAR(255),
            PRIMARY KEY (location_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS property_type (
            property_type_id BIGINT,
            property_type VARCHAR(255),
            PRIMARY KEY (property_type_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS furnishing (
            furnish_state_id BIGINT,
            furnishing VARCHAR(255),
            PRIMARY KEY (furnish_state_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS lease_term (
            lease_term_id BIGINT,
            lease_term VARCHAR(255),
            PRIMARY KEY (lease_term_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS availability (
            availability_id BIGINT,
            availability VARCHAR(255), 
            PRIMARY KEY (availability_id)
        )
        """,        
        """
        CREATE TABLE IF NOT EXISTS property_features (
            feature_id BIGINT,
            feature VARCHAR(255), 
            PRIMARY KEY (feature_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS building_features (
            feature_id BIGINT,
            feature VARCHAR(255),
            PRIMARY KEY (feature_id)
 
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS community_features (
            feature_id BIGINT,
            feature VARCHAR(255),
            PRIMARY KEY (feature_id)

        )
        """,
        """
        CREATE TABLE IF NOT EXISTS tenants (
            tenant_id BIGINT,
            family_members BIGINT,
            full_name VARCHAR(255),
            PRIMARY KEY (tenant_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS properties (
            property_id BIGINT,
            region_id BIGINT,
            city_id BIGINT,
            location_id BIGINT,
            property_type_id BIGINT, 
            furnish_state_id BIGINT, 
            lease_term_id BIGINT, 
            availability_id BIGINT, 
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
            transaction_id BIGINT,
            date TIMESTAMP,
            tenant_id BIGINT,
            property_id BIGINT, 
            PRIMARY KEY (transaction_id),
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (tenant_id) REFERENCES tenants (tenant_id)
        )
        """,   
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT,
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
            log_id BIGINT PRIMARY KEY,
            user_id BIGINT, 
            property_id BIGINT, 
            date TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (property_id) REFERENCES properties (property_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS stay (
            stay_id BIGINT PRIMARY KEY,
            tenant_id BIGINT,
            property_id BIGINT,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,            
            FOREIGN KEY (tenant_id) REFERENCES tenants (tenant_id),
            FOREIGN KEY (property_id) REFERENCES properties (property_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS property_junction (
            property_id BIGINT, 
            feature_id BIGINT,
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (feature_id) REFERENCES property_features (feature_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS building_junction (
            property_id BIGINT, 
            feature_id BIGINT,
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (feature_id) REFERENCES building_features (feature_id)
        )
        """, 
        """
        CREATE TABLE IF NOT EXISTS community_junction (
            property_id BIGINT, 
            feature_id BIGINT,
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (feature_id) REFERENCES community_features (feature_id)
        )
        """                        
        )
