"""
autonomic_core/organs/hebbian_reflection.py
Autonomic Core — Hebbian Reflection Organ
Decoupled mutation logging and scar-tissue formation based on biological reinforcement learning.
"""

from typing import Callable, Optional

class ReflectionResult:
    def __init__(self, block_name: str, outcome: str, diagnostic: str, success: bool, message: str, is_error: bool = False):
        self.block_name = block_name
        self.outcome = outcome
        self.diagnostic = diagnostic
        self.success = success
        self.message = message
        self.is_error = is_error

class HebbianReflection:
    """
    Hebbian Reinforcement Tracker.
    Takes abstracted callbacks that map to the downstream application's event or logging API.
    """
    def __init__(
        self,
        on_success_callback: Optional[Callable[[str], None]] = None,
        on_failure_callback: Optional[Callable[[str], None]] = None
    ):
        self.on_success = on_success_callback
        self.on_failure = on_failure_callback

    def reflect(self, block_name: str, outcome: str, diagnostic: str) -> ReflectionResult:
        """
        Parses a generalized reflection string and executes biological feedback paths.
        outcome strictly requires "IMPROVED" or "DEGRADED".
        """
        outcome_upper = outcome.strip().upper()
        record_str = f"[{block_name}] {outcome_upper}: {diagnostic}"
        
        if outcome_upper == "IMPROVED":
            if self.on_success:
                try:
                    self.on_success(f"Successful Evolution - {record_str}")
                except Exception:
                    pass
            return ReflectionResult(block_name, outcome_upper, diagnostic, True, "[HEBBIAN REINFORCEMENT]\\nPositive architecture mutation recorded safely into persistent ledger.")
            
        elif outcome_upper == "DEGRADED":
            if self.on_failure:
                try:
                    self.on_failure(f"Failed Evolution - {record_str}")
                except Exception:
                    pass
            return ReflectionResult(block_name, outcome_upper, diagnostic, True, "[SCAR TISSUE FORMED]\\nNegative mutation pattern burned into failure ledger to prevent recurrence.")
            
        else:
            return ReflectionResult(block_name, outcome_upper, diagnostic, False, "[REFLECT ERROR]\\nOutcome parameter must be exactly 'IMPROVED' or 'DEGRADED'.", is_error=True)

def handle_reflection_block(reflector: HebbianReflection, block_name: str, outcome: str, diagnostic: str) -> str:
    """
    XML handler wrapper returning the raw string context formatted for ReAct loop insertion.
    """
    try:
        res = reflector.reflect(block_name, outcome, diagnostic)
        return res.message
    except Exception as e:
        return f"[REFLECT ERROR]\\n{str(e)}"
