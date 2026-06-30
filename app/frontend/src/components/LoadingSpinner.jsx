function LoadingSpinner() {
  return (
    <div className="flex flex-col items-center mt-10">

      <div className="w-14 h-14 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>

      <p className="mt-4 text-gray-600 font-medium">
        AI is analyzing the X-ray...
      </p>

    </div>
  );
}

export default LoadingSpinner;