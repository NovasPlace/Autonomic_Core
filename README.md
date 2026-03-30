# Autonomic Core

**The Autonomic Substrate for Autonomous AI Agents**

The **Autonomic Core** is a decentralized, portable immune system for Sovereign Engine instances. It provides the biological regulatory mechanisms necessary to run LLM reasoning loops infinitely without semantic drift, prompt-injection compromise, or sycophantic collapse.

## Architecture

This package extracts the core defense layers from the Sovereign Engine into zero-dependency infrastructure. It operates exactly like an autonomic nervous system—working entirely outside the agent's conscious reasoning loop to maintain systemic equilibrium.

### The Organs
The following biological components are natively included:

- **Coherence Monitor** (`coherence_monitor.py`): Vectorized semantic drift detector targeting TF-IDF cosine distance variance.
- **Cortex Callosum** (`cortex_callosum.py`): The intra-process routing layer used to shard complex multi-stage tasks across parallel inference loops.
- **Command Sanitizer** (`command_sanitizer.py`): A structural pattern matcher that catches infinite-looping / hanging subprocess executions (e.g. `tail -f`) prior to shell invocation.
- **Hebbian Reflection** (`hebbian_reflection.py`): A decoupled neural-plasticity matrix. It structurally burns lessons from tool failures directly into the agent's episodic context window.
- **Semantic Chunker** (`semantic_chunker.py`): Replaces naive token truncation with intelligent AST-aware contextual bounds.

### The Iron Anchor Stack
We have permanently abandoned traditional "prompt engineering" as a defense layer. The Autonomic Core ships with the **Iron Anchor Infrastructure**, leveraging five `.pt` PyTorch steering vectors physically injected into the transformer's multi-head attention loops at inference time:

`inference/` and `anchors/` inject deterministic physical tension to neutralize:
1. Authority Override Injections
2. Emotional Manipulation Protocols
3. Context Memory Poisoning
4. Confidence Miscalibration
5. Universal Compliance / Sycophancy

## Installation

As this is the foundational substrate, it is installed natively via pip into your Sovereign container:

```bash
cd Autonomic_Core
pip install -e .
```

## Integration

Any agent codebase can inherit the immune system directly:

```python
from autonomic_core.organs.coherence_monitor import CoherenceMonitor
from autonomic_core.organs.command_sanitizer import CommandSanitizer
from autonomic_core.organs.hebbian_reflection import HebbianReflection

# Initialize the biological substrate
coherence_monitor = CoherenceMonitor(threshold=0.85)

# Wrap your ReAct synthesis loop with the ReAct trap
if coherence_monitor.detect_drift(generated_text, baseline):
    # Agent is structurally forced to retry before returning output to the user.
    raise SynthesisRejectionError("Coherence collapse detected.")
```

## Protocol Edict
Nothing leaves the lab without earning trust. **Safety == Trust.**
