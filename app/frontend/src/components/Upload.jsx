import { useState } from "react";

function Upload({ onUpload }) {
    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(null);

    const handleChange = (e) => {
        const file = e.target.files[0];

        if (!file) return;

        setImage(file);
        setPreview(URL.createObjectURL(file));
    };

    return (
        <div className="flex flex-col items-center gap-5">

            <input
                type="file"
                accept="image/*"
                onChange={handleChange}
            />

            {preview && (
                <img
                    src={preview}
                    alt="preview"
                    className="w-72 rounded-xl shadow"
                />
            )}

            <button
                onClick={() => onUpload(image)}
                className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700"
            >
                Analyze X-ray
            </button>

        </div>
    );
}

export default Upload;