import numpy as np
from scipy.fftpack import rfft
import peakutils


class featureExtractor:
    def extract(self, x, sound):
        features = []
        for u in range(6):
            features.append(np.mean(x[:100, u]))
            features.append(np.max(x[:100, u]))
            features.append(np.min(x[:100, u]))
            features.append(np.std(x[:100, u]))
            features.append(self.zeroCrossings(x[:100, u]))
            features.append(np.var(x[:100, u]))
            features.append(np.std(x[:100, :3]))
        features.append(np.std(x[:100, 3:]))
        a, b, c, d, e, f, g, h, i = self.topPeaks(sound)
        features.append(a)
        features.append(b)
        features.append(c)
        features.append(d)
        features.append(e)
        features.append(f)
        features.append(g)
        features.append(h)
        features.append(i)
        return features

    def zeroCrossings(x):
        zero_crossings = np.where(np.diff(np.sign(x)))[0]
        return(len(zero_crossings))

    def topPeaks(sound):
        fourier = abs(rfft(sound))
        phase = (np.angle(rfft(sound)))
        indices = peakutils.indexes(fourier, thres=0.02/max(fourier), min_dist=0.1)
        amplitudes = (fourier[indices])
        amplitudes = (np.sort(amplitudes))[len(amplitudes)-3:len(amplitudes)]
        a = fourier.tolist().index(amplitudes[0])
        b = fourier.tolist().index(amplitudes[1])
        c = fourier.tolist().index(amplitudes[2])
        d, e, f = amplitudes
        g = phase[a]
        h = phase[b]
        i = phase[c]
        return a, b, c, d, e, f, g, h, i
