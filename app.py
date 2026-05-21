from flask import Flask, request, jsonify, render_template
from database import init_db, get_connection
from flask_cors import CORS

app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)

CORS(app)
init_db()

@app.route('/')
def home():
    return render_template('index.html')


# =========================
# DRIVERS
# =========================

@app.route('/drivers', methods=['POST'])
def create_driver():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Drivers (Name, LicenseType)
        VALUES (%s, %s)
        RETURNING DriverID
    """, (data['name'], data['license_type']))

    driver_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"DriverID": driver_id})


@app.route('/drivers', methods=['GET'])
def get_drivers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Drivers")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([
        {"DriverID": r[0], "Name": r[1], "LicenseType": r[2]}
        for r in rows
    ])


@app.route('/drivers/<driver_id>', methods=['PUT'])
def update_driver(driver_id):
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Drivers
        SET Name = %s, LicenseType = %s
        WHERE DriverID = %s
    """, (data['name'], data['license_type'], driver_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Updated"})


@app.route('/drivers/<driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Drivers WHERE DriverID = %s", (driver_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Deleted"})


# =========================
# VEHICLES
# =========================

@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Vehicles (LicensePlate, Model, DriverID)
        VALUES (%s, %s, %s)
        RETURNING VehicleID
    """, (data['license_plate'], data['model'], data['driver_id']))

    vehicle_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"VehicleID": vehicle_id})


@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Vehicles")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([
        {"VehicleID": r[0], "LicensePlate": r[1], "Model": r[2], "DriverID": r[3]}
        for r in rows
    ])


@app.route('/vehicles/<vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Vehicles
            SET LicensePlate = %s, Model = %s, DriverID = %s
            WHERE VehicleID = %s
        """, (data['license_plate'], data['model'], data['driver_id'], vehicle_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Updated"})


@app.route('/vehicles/<vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Vehicles WHERE VehicleID = %s", (vehicle_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Deleted"})


# =========================
# ROUTES
# =========================

@app.route('/routes', methods=['POST'])
def create_route():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Routes (Date, ServiceZone, DriverID)
        VALUES (%s, %s, %s)
        RETURNING RouteID
    """, (data['date'], data['service_zone'], data['driver_id']))

    route_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"RouteID": route_id})


@app.route('/routes', methods=['GET'])
def get_routes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Routes")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([
        {"RouteID": r[0], "Date": r[1], "ServiceZone": r[2], "DriverID": r[3]}
        for r in rows
    ])


@app.route('/routes/<route_id>', methods=['PUT'])
def update_route(route_id):
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Routes
        SET Date = %s, ServiceZone = %s, DriverID = %s
        WHERE RouteID = %s
    """, (data['date'], data['service_zone'], data['driver_id'], route_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Updated"})


@app.route('/routes/<route_id>', methods=['DELETE'])
def delete_route(route_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Routes WHERE RouteID = %s", (route_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Deleted"})


# =========================
# PACKAGES
# =========================

@app.route('/packages', methods=['POST'])
def create_package():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Packages (Description, Weight, RouteID)
        VALUES (%s, %s, %s)
        RETURNING PackageID
    """, (data['description'], data['weight'], data['route_id']))

    package_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"PackageID": package_id})


@app.route('/packages', methods=['GET'])
def get_packages():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Packages")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([
        {"PackageID": r[0], "Description": r[1], "Weight": r[2], "RouteID": r[3]}
        for r in rows
    ])


@app.route('/packages/<package_id>', methods=['PUT'])
def update_package(package_id):
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Packages
        SET Description = %s, Weight = %s, RouteID = %s
        WHERE PackageID = %s
    """, (data['description'], data['weight'], data['route_id'], package_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Updated"})


@app.route('/packages/<package_id>', methods=['DELETE'])
def delete_package(package_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Packages WHERE PackageID = %s", (package_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Deleted"})


if __name__ == '__main__':
    app.run(debug=True)