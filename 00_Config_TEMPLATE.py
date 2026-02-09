# ============================================================================
# CONFIGURATION TEMPLATE
# ============================================================================
# Copy this file to 00_Config.py and fill in your values
# Add 00_Config.py to .gitignore to keep your credentials safe

# Your Azure Storage Account
STORAGE_ACCOUNT = "your-storage-account-name"  # Replace with yours

# Your email/username for paths
USER_EMAIL = "your.email@company.com"  # Replace with yours

# Container names
CONTAINER_BRONZE = "bronze"
CONTAINER_SILVER = "silver"
CONTAINER_QUARANTINE = "quarantine"
CONTAINER_AUDIT = "audit"

# ============================================================================
# COMPUTED PATHS (these are built from above settings)
# ============================================================================

# Base path for all data
BASE_PATH = f"abfss://{CONTAINER_BRONZE}@{STORAGE_ACCOUNT}.dfs.core.windows.net"

# Bronze paths
BRONZE_BRIGHTSPACE = f"{BASE_PATH}/bronze/brightspace_enrollments"

# Silver paths
SILVER_BRIGHTSPACE = f"{BASE_PATH}/silver/brightspace_enrollments"

# Quarantine paths
QUARANTINE_BRIGHTSPACE = f"{BASE_PATH}/quarantine/brightspace_enrollments"

# Audit paths
AUDIT_RESOLUTIONS = f"{BASE_PATH}/audit/resolution_history"
AUDIT_METRICS = f"{BASE_PATH}/audit/quality_metrics"

# ============================================================================
# PRINT CONFIGURATION (for verification)
# ============================================================================
print("=" * 70)
print("CONFIGURATION LOADED")
print("=" * 70)
print(f"Storage Account: {STORAGE_ACCOUNT}")
print(f"User: {USER_EMAIL}")
print(f"\nPaths configured:")
print(f"  Bronze:      {BRONZE_BRIGHTSPACE}")
print(f"  Silver:      {SILVER_BRIGHTSPACE}")
print(f"  Quarantine:  {QUARANTINE_BRIGHTSPACE}")
print(f"  Audit:       {AUDIT_RESOLUTIONS}")
print("=" * 70)
