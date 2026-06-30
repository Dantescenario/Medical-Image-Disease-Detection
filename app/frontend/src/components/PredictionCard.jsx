function PredictionCard({ result }) {
  if (!result) return null;

  const isNormal = result.prediction === "NORMAL";

  return (
    <div className="bg-white rounded-3xl shadow-xl p-8 mt-10">

      <h2 className="text-3xl font-bold mb-8">
        Analysis Result
      </h2>

      <div className="flex justify-between items-center">

        <div>

          <p className="text-gray-500">
            Prediction
          </p>

          <span
            className={`inline-block mt-2 px-5 py-2 rounded-full text-white font-bold ${
              isNormal
                ? "bg-green-600"
                : "bg-red-600"
            }`}
          >
            {result.prediction}
          </span>

        </div>

        <div>

          <p className="text-gray-500">
            Confidence
          </p>

          <h3 className="text-3xl font-bold text-blue-700">
            {result.confidence}%
          </h3>

        </div>

      </div>

      <div className="mt-8">

        <div className="w-full bg-gray-200 rounded-full h-5">

          <div
            className="bg-blue-600 h-5 rounded-full"
            style={{ width: `${result.confidence}%` }}
          ></div>

        </div>

      </div>

    </div>
  );
}

export default PredictionCard;