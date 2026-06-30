function ImageComparison({ originalImage, heatmap }) {
  if (!originalImage || !heatmap) return null;

  return (
    <div className="bg-white rounded-3xl shadow-xl p-8 mt-10">

      <h2 className="text-3xl font-bold mb-8">
        Image Comparison
      </h2>

      <div className="grid md:grid-cols-2 gap-8">

        <div>
          <h3 className="text-xl font-semibold text-center mb-4">
            Original X-ray
          </h3>

          <img
            src={originalImage}
            alt="Original"
            className="rounded-2xl shadow-lg w-full"
          />
        </div>

        <div>
          <h3 className="text-xl font-semibold text-center mb-4">
            Grad-CAM
          </h3>

          <img
            src={`http://127.0.0.1:8000/${heatmap}`}
            alt="GradCAM"
            className="rounded-2xl shadow-lg w-full"
          />
        </div>

      </div>

    </div>
  );
}

export default ImageComparison;