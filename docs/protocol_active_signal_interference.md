# Protocol: Active EMF Noise Generation for Hydrogel Dampening

**Abstract**
This protocol documents the use of Software Defined Radio (SDR) to generate localized EMF noise floors. By broadcasting a -32dB noise signal at specific resonant frequencies (2320 MHz, 2400 MHz, 2480 MHz), we can induce a "Static State" in the hydrogel lattice, effectively attenuating its electromechanical response and preventing signal-induced turgor.

---

## 1. The Theory of Resonant Dampening
Hydrogel networks are tuned to specific carrier frequencies within the microwave spectrum. 
* **Harmonic Interference:** By flooding the immediate environment with a low-power noise floor (-32dB), we create "destructive interference" within the hydrogel's internal harvesting circuit.
* **The Static State:** The hydrogel becomes overwhelmed by the noise, losing its ability to distinguish and transduce the structured pulses of the "attacker" signal.

---

## 2. Hardware & Command Specs
* **Device:** HackRF One (or similar SDR).
* **Software:** `hackrf_transfer` (standard SDR library).

### 2.1 Targeted Frequencies
1. **2320 MHz:** Lower-band resonance dampening.
2. **2400 MHz:** Standard WiFi/Bluetooth band overlap (high harvesting area).
3. **2480 MHz:** Upper-band resonance dampening.

### 2.2 Execution Command
```bash
# Example command for generating Gaussian noise at 2320, 2400, 2480 MHz.
- first generate the noise_sample.bin file using this command:
  hackrf_transfer -r noise_sample.bin -f 2400000000 -s 20000000 -n 20000000 -l 32 -g 40 -a 0

- then run the noise sample on one of the following:
hackrf_transfer -t noise_sample.bin -f 2320000000 -s 20000000 -x 47 -a 0 -R
hackrf_transfer -t noise_sample.bin -f 2400000000 -s 20000000 -x 47 -a 0 -R
hackrf_transfer -t noise_sample.bin -f 2480000000 -s 20000000 -x 47 -a 0 -R





