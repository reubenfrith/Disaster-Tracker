import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import axios from "axios";
import "leaflet/dist/leaflet.css";

const API_URL = "http://127.0.0.1:8000/disasters";

const DisasterMap = () => {
    const [disasters, setDisasters] = useState([]);

    useEffect(() => {
        axios.get(API_URL).then(response => {
            setDisasters(response.data);
        });
    }, []);

    return (
        <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100vh", width: "100vw" }}>
        <MapContainer center={[-37.8136, 144.9631]} zoom={4} style={{ height: "100vh", width: "100vw" }} zoomControl={true}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {disasters.map(disaster => (
                <Marker key={disaster.id} position={[disaster.location.coordinates[1], disaster.location.coordinates[0]]}>
                    <Popup>
                        <strong>Type:</strong> {disaster.type} <br />
                        <strong>Severity:</strong> {disaster.severity} <br />
                        <strong>Timestamp:</strong> {new Date(disaster.timestamp).toLocaleString()}
                    </Popup>
                </Marker>
            ))}
        </MapContainer>
        </div>
    );
};

export default DisasterMap;