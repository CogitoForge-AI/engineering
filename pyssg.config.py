from __future__ import annotations

import os

from pyssg.presets import blog

config = blog(
    site={
        "title": "Cogito Engineering",
        "description": "Essays, field notes, and practical lessons from the engineers building products, AI systems, and internal platforms at Cogito.",
        "tagline": "Engineering writing from Cogito teams working across AI, product systems, reliability, and delivery.",
        "organization": "Cogito AI",
        "github_org_url": "https://github.com/cogitoForge-AI",
        "github_url": "https://github.com/cogitoForge-AI/engineering",
        "feed_url": "/feed.xml",
        "brand_logo": "/assets/brand/logo-horizontal.png",
        "brand_icon": "/assets/brand/icon.png",
    },
    base_url="https://engineering.cogito-ai.org",
    layout="layouts/theme",
    deploy={
        "github-pages": {
            "repo": os.getenv("GITHUB_REPOSITORY", "cogitoForge-AI/engineering"),
            "cname": "engineering.cogito-ai.org",
        },
    },
)
