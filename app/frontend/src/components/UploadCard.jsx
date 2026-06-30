import { useState } from "react";


function UploadCard({ onUpload, loading }) {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleChange = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  return (
    <div className="bg-white rounded-3xl shadow-xl p-8">

      <label
        htmlFor="image-upload"
        className="border-2 border-dashed border-blue-300 rounded-2xl p-10 flex flex-col items-center justify-center cursor-pointer hover:border-blue-500 hover:bg-blue-50 transition-all duration-300"
      >

        <div className="text-6xl">
    📤
</div>

        <p className="mt-4 text-xl font-semibold">
          Upload Chest X-ray
        </p>

        <p className="text-gray-500 mt-2">
          Click to browse your computer
        </p>

        <input
          id="image-upload"
          type="file"
          accept="image/*"
          onChange={handleChange}
          className="hidden"
        />

      </label>

      {preview && (
        <div className="mt-8 flex justify-center">

          <img
            src={preview}
            alt="Preview"
            className="rounded-2xl shadow-lg max-h-96"
          />

        </div>
      )}

      <div className="flex justify-center mt-8">

        <button
          disabled={!image || loading}
          onClick={() => onUpload(image, preview)}
          className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-10 py-4 rounded-xl text-lg font-semibold transition-all duration-300"
        >
          {loading ? "Analyzing..." : "Analyze X-ray"}
        </button>

      </div>

    </div>
  );
}

export default UploadCard;