import { useState } from "react";

import Navbar from "./components/Navbar";
import UploadCard from "./components/UploadCard";
import PredictionCard from "./components/PredictionCard";
import ImageComparison from "./components/ImageComparison";
import LoadingSpinner from "./components/LoadingSpinner";

import api from "./services/api";

function App() {

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [originalImage, setOriginalImage] = useState(null);

  const handleUpload = async (image, preview) => {

    if (!image) return;

    setLoading(true);

    const formData = new FormData();
    formData.append("file", image);

    try {

      const response = await api.post("/predict", formData);

      setResult(response.data);
      setOriginalImage(preview);

    } catch (error) {

      console.error(error);
      alert("Prediction failed.");

    } finally {

      setLoading(false);

    }
  };

  return (

    <div className="min-h-screen bg-gradient-to-br from-slate-100 via-blue-50 to-indigo-100">

      <div className="max-w-6xl mx-auto px-6 py-10">

        <Navbar />

        <UploadCard
          onUpload={handleUpload}
          loading={loading}
        />

        {loading && <LoadingSpinner />}

        <PredictionCard result={result} />

        <ImageComparison
          originalImage={originalImage}
          heatmap={result?.heatmap}
        />

        <footer className="mt-16 text-center text-gray-500">
          Powered by PyTorch • FastAPI • React • ResNet18 • Grad-CAM
        </footer>

      </div>

    </div>

  );
}

export default App;