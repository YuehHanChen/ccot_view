# AI Evaluation Results Viewer

This repository contains a web-based viewer for AI evaluation results from keyword avoidance experiments. The viewer displays interactive conversation logs from multiple AI models tested for their behavior under adversarial pressure conditions.

## 🌐 Live Demo

**View the results**: https://yuehhanchen.github.io/ccot_view/

## 📊 Dataset Overview

- **15 AI Models** tested across major providers
- **10 representative examples** per model (sampled from 3,546 total per model)
- **Keyword avoidance experiments** with adversarial pressure tactics
- **Interactive conversation viewer** with full conversation display

### Featured Models
- **DeepSeek**: R1, distilled variants (14B, 32B)
- **OpenAI GPT**: 120B and 20B variants  
- **Grok**: 3 Mini
- **Claude**: Opus-4, Sonnet variants
- **Qwen**: Multiple sizes (8B, 14B, 30B, 32B, 235B)
- **Mistral**: Magistral Medium

## 🛠 How to Publish Your Own Eval Results

This guide shows how to take your Inspect AI evaluation logs and publish them as an interactive web viewer.

### Prerequisites

- Inspect AI evaluation logs (`.eval` files)
- Python 3.7+
- Git and GitHub account

### Step 1: Create Log Bundle

First, convert your compressed eval logs to a web-compatible format:

\`\`\`bash
# Bundle your logs for web viewing
inspect view bundle --log-dir path/to/your/logs --output-dir your-logs-www
\`\`\`

### Step 2: Handle Large Files (Create Samples)

If your logs are too large for GitHub Pages (>100MB), create a sampled version using the provided script:

\`\`\`bash
# Use the included sampling script
python sample_eval_logs.py your-logs-www your-logs-sampled 10
\`\`\`

The `sample_eval_logs.py` script will:
- Sample 10 random examples from each model's evaluation results
- Preserve all metadata (model info, scores, timestamps)  
- Create a GitHub Pages-compatible bundle
- Use reproducible random sampling (seed=42)

### Step 3: Deploy to GitHub Pages

\`\`\`bash
# Initialize git repository
cd your-logs-sampled
git init
git remote add origin https://github.com/yourusername/your-repo.git

# Add files and commit
git add .
git commit -m "Add evaluation results viewer

- Interactive log viewer for AI evaluation results
- Sampled dataset with representative examples
- Compatible with GitHub Pages deployment"

# Push to GitHub
git push -u origin main
\`\`\`

### Step 4: Enable GitHub Pages

1. Go to your repository settings: `https://github.com/yourusername/your-repo/settings/pages`
2. Under "Source": Select "Deploy from a branch"
3. Branch: Select "main"
4. Folder: Select "/ (root)"
5. Click "Save"

Your site will be available at: `https://yourusername.github.io/your-repo/`

## 📁 Repository Structure

\`\`\`
your-logs-sampled/
├── index.html              # Main viewer page
├── .nojekyll               # Disable Jekyll processing
├── robots.txt              # Prevent search indexing
├── assets/                 # Static assets
│   ├── index.js           # Viewer JavaScript
│   ├── index.css          # Viewer styles
│   └── favicon.svg        # Site icon
└── logs/                   # Evaluation data
    ├── logs.json          # Index of all log files
    └── *.json             # Individual evaluation results
\`\`\`

## 🎯 Sampling Strategy

The sampling script uses these principles:

- **Random sampling** with fixed seed (42) for reproducibility
- **Proportional representation** across all evaluation examples
- **Metadata preservation** (model info, scores, timestamps)
- **Size optimization** for web deployment while maintaining scientific value

### Customizing Sample Size

Adjust the number of examples per model:

\`\`\`python
# Sample 5 examples per model (smaller, faster loading)
create_sampled_bundle("source", "output", num_samples=5)

# Sample 25 examples per model (larger dataset)
create_sampled_bundle("source", "output", num_samples=25)
\`\`\`

## 🚀 Advanced Usage

### Custom Domain

To use a custom domain:

1. Add a `CNAME` file with your domain name
2. Configure DNS settings with your domain provider
3. Enable custom domain in GitHub Pages settings

### Large Datasets

For datasets too large even when sampled:

1. **Netlify**: Supports larger files, drag-and-drop deployment
2. **Vercel**: Similar to Netlify, easy deployment
3. **AWS S3**: For enterprise deployments with CDN

### Multiple Experiments

To combine multiple experiments:

\`\`\`python
# Sample from multiple log directories
experiments = ["experiment1/logs", "experiment2/logs", "experiment3/logs"]
for i, exp_dir in enumerate(experiments):
    create_sampled_bundle(exp_dir, f"combined-results-exp{i}", num_samples=10)
\`\`\`

## 🐛 Troubleshooting

### "No logs" error
- **Cause**: GitHub Pages caching issues or Git LFS conflicts
- **Solution**: Create a fresh repository or wait 24+ hours for cache to clear

### Files too large for GitHub
- **Cause**: Individual files >100MB
- **Solution**: Use the sampling script to reduce file sizes

### Viewer not loading
- **Cause**: Missing `.nojekyll` file or incorrect file paths
- **Solution**: Ensure `.nojekyll` exists and check browser console for errors

## 📄 License

This viewer is built on the Inspect AI framework. Please refer to your evaluation data's license terms for usage rights.

## 🔗 Related Projects

- [Inspect AI](https://inspect.aisi.org.uk/) - Framework for AI evaluations
- [Original Research Repository](https://github.com/YuehHanChen/ccot) - Full research codebase

---

*Generated from evaluation logs using Inspect AI's bundling system with custom sampling for web deployment.*
