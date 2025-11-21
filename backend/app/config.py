# backend/app/config.py
from pathlib import Path
import os
# Base dir is .../gpr_model
BASE_DIR = Path(__file__).resolve().parents[2]

ARTIFACTS_DIR = BASE_DIR / "artifacts"
DATA_DIR      = BASE_DIR / "data"

# Main feature table (from your notebook export)
FEAT_DF_CSV   = ARTIFACTS_DIR / "feat_df_all_vehicles.csv"

# Later we’ll also use:
FEATURES_CFG_JSON = ARTIFACTS_DIR / "features_f1.json"
SEQ2SEQ_MODEL     = ARTIFACTS_DIR / "seq2seq1_f1.keras"
GPR_RESIDUAL_PKL  = ARTIFACTS_DIR / "gpr_residual.pkl"
CA_SCALER_PKL     = ARTIFACTS_DIR / "ca_scaler.pkl"
F_SCALER_PKL      = ARTIFACTS_DIR / "f_scaler.pkl"
X2_SCALER_PKL     = ARTIFACTS_DIR / "x2_scaler.pkl"

SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
SMTP_FROM = os.getenv("SMTP_FROM") or SMTP_USER
