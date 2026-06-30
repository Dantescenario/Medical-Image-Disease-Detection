function Result({ result }) {
    if (!result) return null;

    return (
        <div className="mt-10 bg-white shadow-lg rounded-xl p-6 w-full max-w-md">

            <h2 className="text-2xl font-bold mb-4">
                Analysis Result
            </h2>

            <p className="text-lg">
                <strong>Prediction:</strong> {result.prediction}
            </p>

            <p className="text-lg">
                <strong>Confidence:</strong> {result.confidence}%
            </p>

            {result.heatmap && (
                <div className="mt-6">
                    <img
                        src={`http://127.0.0.1:8000/${result.heatmap}`}
                        alt="GradCAM"
                        className="rounded-lg shadow"
                    />
                </div>
            )}

        </div>
    );
}

export default Result;