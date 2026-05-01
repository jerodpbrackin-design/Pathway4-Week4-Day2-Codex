import psycopg2

DB_CONFIG = {
    "database": "db_jman",
    "user": "jman",
    "password": "jman_pass",
    "host": "pathway-4.ca1yc8okmo57.us-east-1.rds.amazonaws.com",
    "port": "5432"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Drivers (
        DriverID UUID PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        LicenseType VARCHAR(25)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vehicles (
        VehicleID UUID PRIMARY KEY,
        LicensePlate VARCHAR(10),
        Model VARCHAR(25),
        DriverID UUID UNIQUE,
        FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Routes (
        RouteID UUID PRIMARY KEY,
        Date TIMESTAMP,
        ServiceZone VARCHAR(50),
        DriverID UUID,
        FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Packages (
        PackageID UUID PRIMARY KEY,
        Description VARCHAR(50) NOT NULL,
        Weight DECIMAL(10,2) NOT NULL,
        RouteID UUID,
        FOREIGN KEY (RouteID) REFERENCES Routes(RouteID)
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()