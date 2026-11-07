# Render deployment

Deploy the backend as a **Python Web Service**, using the repository root as
the Root Directory (leave the field blank). The root package.json belongs to
neither the backend nor the frontend build; do not deploy the API as Node.

Use render.yaml as a Render Blueprint, or configure an existing service:

- Build command: `pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cpu && pip install -r requirements.txt`
- Start command: `uvicorn app.backend.main:app --host 0.0.0.0 --port $PORT`
- Environment: `PYTHON_VERSION=3.11.11`
- Environment: `CORS_ORIGINS=https://your-frontend-domain.example` (comma-separated origins, without trailing slashes)
- Health check path: `/`

The CPU PyTorch packages avoid downloading unnecessary CUDA libraries. The
tracked file outputs/best_model.pth must be included in the deployment.
Inference loads this checkpoint directly without downloading ImageNet weights.
ML dependencies initialize on the first prediction request so they do not delay
port binding. That request can take longer while the model and Matplotlib font
cache initialize. The root health check confirms HTTP availability, not model
readiness.

Deploy the frontend separately as a static site:

- Root Directory: `app/frontend`
- Build command: `npm ci && npm run build`
- Publish directory: `dist`
- Build environment: `VITE_API_URL=https://your-api.onrender.com`

Rebuild the frontend after changing VITE_API_URL. Set the API's CORS_ORIGINS
to the final frontend origin. vercel.json does not configure Render.

If deployment still fails, inspect the first error in Render's build/runtime
logs. An out-of-memory termination requires measuring runtime memory and
selecting an instance with sufficient RAM; CPU wheels reduce installation size
but do not guarantee the model fits a particular instance.
