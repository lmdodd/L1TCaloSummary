import os
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("L1TCaloSummaryTest", eras.Run2_2016)

import EventFilter.L1TXRawToDigi.util as util

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing()
options.register('runNumber', 0, VarParsing.multiplicity.singleton, VarParsing.varType.int, 'Run to analyze')
options.register('lumis', '1-max', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'Lumis')
options.register('dataStream', '/ExpressPhysics/Run2015D-Express-v4/FEVT', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'Dataset to look for run in')
options.register('inputFiles', [], VarParsing.multiplicity.list, VarParsing.varType.string, 'Manual file list input, will query DAS if empty')
options.register('inputFileList', '', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'Manual file list input, will query DAS if empty')
options.register('useORCON', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'Use ORCON for conditions.  This is necessary for very recent runs where conditions have not propogated to Frontier')
options.register('maxEvents', 10000, VarParsing.multiplicity.singleton, VarParsing.varType.int, 'Maximum number of events to process')
options.parseArguments()

def formatLumis(lumistring, run) :
    lumis = (lrange.split('-') for lrange in lumistring.split(','))
    runlumis = (['%d:%s' % (run,lumi) for lumi in lrange] for lrange in lumis)
    return ['-'.join(l) for l in runlumis]

print 'Getting files for run %d...' % options.runNumber
if len(options.inputFiles) is 0 and options.inputFileList is '' :
    inputFiles = util.getFilesForRun(options.runNumber, options.dataStream)
elif len(options.inputFileList) > 0 :
    with open(options.inputFileList) as f :
        inputFiles = list((line.strip() for line in f))
else :
    inputFiles = cms.untracked.vstring(options.inputFiles)
if len(inputFiles) is 0 :
    raise Exception('No files found for dataset %s run %d' % (options.dataStream, options.runNumber))
print 'Ok, time to analyze'

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2016Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# To get L1 CaloParams
process.load('L1Trigger.L1TCalorimeter.caloStage2Params_2016_v2_1_cfi')
# To get CaloTPGTranscoder
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')

process.load('EventFilter.L1TXRawToDigi.caloLayer1Stage2Digis_cfi')

process.load('L1Trigger.L1TCaloSummary.uct2016EmulatorDigis_cfi')
process.uct2016EmulatorDigis.useECALLUT = cms.bool(True)
process.uct2016EmulatorDigis.useHCALLUT = cms.bool(True)
process.uct2016EmulatorDigis.useHFLUT = cms.bool(True)
process.uct2016EmulatorDigis.useLSB = cms.bool(True)
process.uct2016EmulatorDigis.verbose = cms.bool(False)
process.uct2016EmulatorDigis.ecalToken = cms.InputTag("l1tCaloLayer1Digis")
process.uct2016EmulatorDigis.hcalToken = cms.InputTag("l1tCaloLayer1Digis")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(inputFiles)
)

outputFile = '/data/' + os.environ['USER'] + '/l1tCaloSummary-' + str(options.runNumber) + '.root'

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(outputFile),
    outputCommands = cms.untracked.vstring('drop *', 'keep *_*_*_L1TCaloSummaryTest')
)

process.p = cms.Path(process.l1tCaloLayer1Digis*process.uct2016EmulatorDigis)

process.e = cms.EndPath(process.out)
