# Use a specific, pinned Python version
FROM python:3.10.12-slim AS base

# ---- stage: build (install system deps & python deps) ----
FROM base AS build

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed for some Python packages (adjust as needed)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc libpq-dev curl && rm -rf /var/lib/apt/lists/*

# Copy dependency spec and install
COPY requirements.txt .
# Upgrade pip first (optional)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && pip install --no-cache-dir -r requirements.txt

# ---- stage: final (minimal runtime image) ----
FROM base AS final

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Create a non-root user
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /app

# Copy only installed site-packages and app files from build stage
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy application source
COPY . .

# Change ownership to non-root user and switch
RUN chown -R appuser:appuser /app
USER appuser

# Example healthcheck (optional)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s CMD curl -f http://localhost:8501/ || exit 1

# Default command: override based on whether this image is for Streamlit or ETL
# For development you might want: CMD ["bash"]
# For Streamlit dashboard:
CMD ["streamlit", "run", "dashboard/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
