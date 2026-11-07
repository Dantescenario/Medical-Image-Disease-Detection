import axios from "axios";

export const API_BASE_URL = (
    import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"
).replace(/\/+$/, "");

export const getHeatmapUrl = (path) => `${API_BASE_URL}/${path.replace(/^\/+/, "")}`;

const api = axios.create({ baseURL: API_BASE_URL });

export default api;
