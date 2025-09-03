#!/usr/bin/env python3
"""
Railway-optimized startup script for HackRx LLM system
"""

import os
import sys
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Main startup function optimized for Railway"""
    
    # Get port from environment - Railway automatically sets this
    port = int(os.getenv("PORT", 8080))
    
    # Log startup info
    logger.info("=" * 50)
    logger.info("🚀 STARTING HACKRX LLM SYSTEM")
    logger.info(f"📡 Port: {port}")
    logger.info(f"🐍 Python: {sys.version}")
    logger.info(f"🌍 Host: 0.0.0.0 (required for Railway)")
    logger.info("=" * 50)
    
    try:
        # Import here to ensure all dependencies are loaded
        from main import app
        
        # Run with Railway-optimized settings
        uvicorn.run(
            app,
            host="0.0.0.0",  # Critical for Railway - must be 0.0.0.0
            port=port,
            log_level="info",
            access_log=True,
            loop="asyncio",
            # Railway-specific optimizations
            timeout_keep_alive=30,
            limit_concurrency=50,
            limit_max_requests=500,
            timeout_graceful_shutdown=30,
        )
        
    except ImportError as e:
        logger.error(f"❌ Import error: {e}")
        logger.error("Make sure all dependencies are installed")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Startup error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
