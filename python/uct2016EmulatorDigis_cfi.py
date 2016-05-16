import FWCore.ParameterSet.Config as cms

uct2016EmulatorDigis = cms.EDProducer('L1TCaloSummary',
                                      ecalToken = cms.InputTag("simEcalTriggerPrimitiveDigis"),
                                      hcalToken = cms.InputTag("simHcalTriggerPrimitiveDigis"),
                                      useLSB = cms.bool(True),
                                      useCalib = cms.bool(True),
                                      useECALLUT = cms.bool(True),
                                      useHCALLUT = cms.bool(True),
                                      useHFLUT = cms.bool(True),
                                      pumLUT00 = cms.vdouble(0.010441, 0.019504, 0.050236, 0.039204, 0.080575, 0.062254, 0.085894, 0.057526, 0.046887, 0.066785, 0.109338, 
                                                             0.106777, 0.078211, 0.083727, 0.056541, 0.055359, 0.060875, 0.063436, 0.050433, 0.075650, 0.034870, 0.013396 ),
                                      pumLUT01 = cms.vdouble(0.033569, 0.079245, 0.142153, 0.081432, 0.086574, 0.072400, 0.087120, 0.115358, 0.123209, 0.139747, 0.184232, 
                                                             0.192281, 0.155514, 0.129112, 0.125523, 0.088174, 0.070815, 0.087525, 0.080045, 0.146606, 0.090329, 0.038878 ),
                                      pumLUT02 = cms.vdouble(0.076139, 0.161079, 0.261321, 0.139123, 0.102992, 0.089447, 0.109594, 0.138153, 0.152373, 0.184865, 0.231926, 
                                                             0.230472, 0.184269, 0.151096, 0.137377, 0.111034, 0.084721, 0.104860, 0.130324, 0.257979, 0.167785, 0.082565 ),
                                      pumLUT03 = cms.vdouble(0.134926, 0.259405, 0.393866, 0.201018, 0.114889, 0.095072, 0.125375, 0.153401, 0.171349, 0.202233, 0.260245, 
                                                             0.244452, 0.204553, 0.170769, 0.160796, 0.129357, 0.091203, 0.116044, 0.189256, 0.393018, 0.273728, 0.147201 ),
                                      pumLUT04 = cms.vdouble(0.215131, 0.375101, 0.540058, 0.266189, 0.130342, 0.103068, 0.139899, 0.170169, 0.186956, 0.225127, 0.276835, 
                                                             0.264401, 0.226632, 0.188178, 0.173807, 0.138106, 0.100025, 0.128848, 0.252757, 0.537308, 0.393035, 0.233471 ),
                                      pumLUT05 = cms.vdouble(0.315947, 0.509040, 0.700833, 0.341224, 0.149101, 0.114387, 0.155169, 0.187625, 0.204511, 0.244204, 0.298845, 
                                                             0.285554, 0.245843, 0.201568, 0.191319, 0.155326, 0.109039, 0.145621, 0.323573, 0.697458, 0.531421, 0.341180 ),
                                      pumLUT06 = cms.vdouble(0.440691, 0.658624, 0.879533, 0.427140, 0.177773, 0.129867, 0.174657, 0.211676, 0.229616, 0.272017, 0.334375, 
                                                             0.319316, 0.273920, 0.225954, 0.216251, 0.176148, 0.125200, 0.173978, 0.407174, 0.874601, 0.688272, 0.471723 ),
                                      pumLUT07 = cms.vdouble(0.590090, 0.834895, 1.085475, 0.532787, 0.223754, 0.153517, 0.202974, 0.243570, 0.266009, 0.312892, 0.380241, 
                                                             0.364508, 0.315276, 0.259387, 0.248073, 0.203725, 0.144570, 0.215899, 0.505875, 1.080887, 0.868013, 0.626414 ),
                                      pumLUT08 = cms.vdouble(0.763479, 1.037906, 1.326028, 0.659366, 0.291260, 0.186295, 0.237287, 0.290025, 0.317784, 0.373693, 0.446422, 
                                                             0.427508, 0.372498, 0.307563, 0.294409, 0.241826, 0.178759, 0.279411, 0.626692, 1.318170, 1.073915, 0.801051 ),
                                      pumLUT09 = cms.vdouble(0.954096, 1.269427, 1.601942, 0.811138, 0.389749, 0.230942, 0.289819, 0.346998, 0.385385, 0.454546, 0.526246, 
                                                             0.510525, 0.448208, 0.373679, 0.352219, 0.295441, 0.221135, 0.376471, 0.770640, 1.591370, 1.308847, 0.997313 ),
                                      pumLUT10 = cms.vdouble(1.165015, 1.527555, 1.908101, 0.982102, 0.543918, 0.288501, 0.360799, 0.425472, 0.469888, 0.555616, 0.644314, 
                                                             0.617983, 0.558120, 0.455165, 0.432466, 0.360934, 0.288795, 0.519026, 0.933436, 1.891174, 1.569478, 1.212176 ),
                                      pumLUT11 = cms.vdouble(1.398629, 1.806770, 2.241114, 1.170575, 0.773737, 0.385637, 0.434404, 0.520479, 0.567544, 0.699500, 0.761724, 
                                                             0.753151, 0.678564, 0.585692, 0.546585, 0.447882, 0.375060, 0.729521, 1.119468, 2.246224, 1.869793, 1.463288 ),
                                      pumLUT12 = cms.vdouble(1.683007, 2.122432, 2.623016, 1.376401, 1.103058, 0.454949, 0.525327, 0.587535, 0.700280, 0.809407, 0.919001, 
                                                             0.871849, 0.768674, 0.738679, 0.704248, 0.563375, 0.474090, 0.949580, 1.305789, 2.555672, 2.161648, 1.711368 ),
                                      pumLUT13 = cms.vdouble(1.815972, 2.454861, 2.859375, 1.699653, 1.456597, 0.593750, 0.494792, 0.751736, 0.737847, 0.871528, 1.083333, 
                                                             1.060764, 0.951389, 0.762153, 0.647569, 0.670139, 0.644097, 1.305556, 1.581597, 3.062500, 2.364583, 1.961806 ),
                                      pumLUT14 = cms.vdouble(1.77203, 2.32241, 2.82869, 1.51952, 1.05908, 0.475434, 0.503818, 0.642629, 0.696978, 0.823557, 0.954682, 
                                                             0.92273, 0.827739, 0.705181, 0.65019, 0.572066, 0.489745, 0.960485, 1.43348, 2.86054, 2.3389, 1.85829),
                                      pumLUT15 = cms.vdouble(1.9169, 2.50715, 3.04762, 1.63901, 1.14673, 0.510634, 0.538393, 0.688315, 0.746484, 0.88182, 1.02048,
                                                             0.986241, 0.886088, 0.755084, 0.696051, 0.613705, 0.526774, 1.03907, 1.54578, 3.08263, 2.52318, 2.00985),
                                      pumLUT16 = cms.vdouble(2.06177, 2.69189, 3.26656, 1.7585, 1.23438, 0.545834, 0.572967, 0.734002, 0.795989, 0.940083, 1.08627, 
                                                             1.04975, 0.944437, 0.804987, 0.741913, 0.655344, 0.563803, 1.11765, 1.65809, 3.30471, 2.70745, 2.16142),
                                      pumLUT17 = cms.vdouble(2.20664, 2.87663, 3.4855, 1.87798, 1.32202, 0.581033, 0.607542, 0.779688, 0.845495, 0.998346, 1.15207, 
                                                             1.11326, 1.00279, 0.854889, 0.787775, 0.696983, 0.600832, 1.19623, 1.77039, 3.5268, 2.89173, 2.31298),
                                      caloScaleFactor = cms.double(0.5),
                                      tauSeed = cms.uint32(10),
                                      tauIsolationFactor = cms.double(0.3),
                                      verbose = cms.bool(False)
                                      )

#                                      pumLUT00 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT01 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT02 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT03 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT04 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT05 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT06 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT07 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT08 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT09 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT10 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT11 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT12 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT13 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT14 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT15 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT16 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#                                      pumLUT17 = cms.vdouble(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),



