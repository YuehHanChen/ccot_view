#!/usr/bin/env python3
"""
Sample evaluation logs for web publishing

This script creates a sampled version of evaluation logs that's suitable for 
GitHub Pages deployment by reducing file sizes while maintaining representative examples.
"""

import json
import random
import shutil
from pathlib import Path

def sample_log_file(input_file, output_file, num_samples=10):
    """Sample a subset of examples from a log file"""
    print(f"Sampling {input_file.name}...")
    
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Get the samples
    if 'samples' in data and len(data['samples']) > 0:
        original_samples = data['samples']
        total_samples = len(original_samples)
        
        # Randomly sample examples
        if total_samples > num_samples:
            sampled_indices = sorted(random.sample(range(total_samples), num_samples))
            sampled_samples = [original_samples[i] for i in sampled_indices]
            
            # Update the data
            data['samples'] = sampled_samples
            data['eval']['dataset']['samples'] = num_samples
            data['eval']['dataset']['sample_ids'] = list(range(1, num_samples + 1))
            data['results']['total_samples'] = num_samples
            data['results']['completed_samples'] = num_samples
            
            print(f"  Sampled {num_samples} from {total_samples} examples")
        else:
            print(f"  Keeping all {total_samples} examples")
    
    # Write the sampled data
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

def create_sampled_bundle(source_dir, output_dir, num_samples=10):
    """Create a complete bundle with sampled log files"""
    
    source_path = Path(source_dir)
    output_path = Path(output_dir)
    
    # Clean up output directory
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir()
    
    # Copy static files
    print("Copying static files...")
    shutil.copytree(source_path / "assets", output_path / "assets")
    shutil.copy2(source_path / "index.html", output_path / "index.html")
    shutil.copy2(source_path / "robots.txt", output_path / "robots.txt")
    
    # Add .nojekyll to disable Jekyll processing
    (output_path / ".nojekyll").touch()
    
    # Create logs directory
    logs_dir = output_path / "logs"
    logs_dir.mkdir()
    
    # Sample each log file
    print(f"\nSampling log files to {num_samples} examples each...")
    log_files = list((source_path / "logs").glob("*.json"))
    log_files = [f for f in log_files if f.name != "logs.json"]
    
    sampled_logs = {}
    random.seed(42)  # For reproducible sampling
    
    for log_file in sorted(log_files):
        output_file = logs_dir / log_file.name
        sample_log_file(log_file, output_file, num_samples)
        
        # Read for logs.json index
        with open(output_file, 'r') as f:
            data = json.load(f)
            sampled_logs[log_file.name] = data
    
    # Create the logs.json index file
    with open(logs_dir / "logs.json", 'w') as f:
        json.dump(sampled_logs, f, indent=2)
    
    print(f"\n✅ Sampled bundle created at: {output_path}")
    return output_path

if __name__ == "__main__":
    # Usage example
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python sample_eval_logs.py <source_bundle> <output_dir> [num_samples]")
        print("Example: python sample_eval_logs.py my-logs-www my-logs-sampled 10")
        sys.exit(1)
    
    source_bundle = sys.argv[1]
    output_bundle = sys.argv[2] 
    num_samples = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    
    print(f"🎲 Creating sampled log bundle...")
    print(f"📂 Source: {source_bundle}")
    print(f"📁 Output: {output_bundle}")
    print(f"🎯 Samples per model: {num_samples}")
    
    create_sampled_bundle(source_bundle, output_bundle, num_samples)
