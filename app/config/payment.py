"""
app/config/payment.py — Cafe Song Han Module
"""
from __future__ import annotations
import os

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
