from PyQt5 import QtWidgets
import sys
from design import Ui_LaserCalculator
from program import calc
import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_LaserCalculator()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate)



    def calculate(self):
        # input variables : this section imports all the user input parameters
        # and stores them in python variables

        transmittingPower = self.ui.transmittingPower.text()
        wavelength = self.ui.wavelength.text()
        divergenceAngle = self.ui.divergenceAngle.text()
        linkRange = self.ui.linkRange.text()
        receiverDiameter = self.ui.receiverDiameter.text()
        focalLength = self.ui.focalLength.text()
        opticaTransmittance = self.ui.opticaTransmittance.text()
        darkCurrent = self.ui.darkCurrent.text()
        bandwidth = self.ui.bandwidth.text()
        loadResistance = self.ui.loadResistance.text()
        responsivity = self.ui.responsivity.text()
        visibility = self.ui.visibility.text()
        q = self.ui.q.text()
        solarRadiance = self.ui.solarRadiance.text()
        opticalFilterBandwidth = self.ui.opticalFilterBandwidth.text()
        beamWaist = self.ui.beamWaist.text()

        #following section converts string inputs to float values

        transmittingPower = float(transmittingPower)
        wavelength = float(wavelength)
        divergenceAngle = float(divergenceAngle)
        linkRange = float(linkRange)
        receiverDiameter = float(receiverDiameter)
        focalLength = float(focalLength)
        opticaTransmittance = float(opticaTransmittance)
        darkCurrent = float(darkCurrent)
        bandwidth = float(bandwidth)
        loadResistance = float(loadResistance)
        responsivity = float(responsivity)
        visibility = float(visibility)
        q = float(q)
        solarRadiance = float(solarRadiance)
        opticalFilterBandwidth = float(opticalFilterBandwidth)
        beamWaist = float(beamWaist)


        # output variables : calculation formulas in the following section
        # edit the following section as per required, based on testing

        areaReceivingLens_AR = (3.14) / (4 * (receiverDiameter ** 2))
        receiverBeamDiameter_Dl = divergenceAngle*linkRange + beamWaist
        receiverBeamArea_AB = (3.14/4)*(receiverBeamDiameter_Dl**2)
        beamDivergenceLoss_Tbdl = areaReceivingLens_AR/receiverBeamArea_AB
        atmosphericExtinctionCoefficient_alpha = (3.91/visibility)*((wavelength/550)**-q)
        atmosphericTransmittance_Tatm = np.exp(-atmosphericExtinctionCoefficient_alpha*linkRange)
        receivedPower_PR = opticaTransmittance*transmittingPower*atmosphericTransmittance_Tatm*beamDivergenceLoss_Tbdl
        receivingLensFOV = receiverDiameter / focalLength
        solidAngle = ((3.14) / 4) * (receivingLensFOV ** 2)
        receivedsolarPower_Ps = solarRadiance * solidAngle * areaReceivingLens_AR * opticalFilterBandwidth
        CurrentDueToSignal_Ir = receivedPower_PR*responsivity
        currentDueToSignalAndSBR_It = CurrentDueToSignal_Ir+(receivedsolarPower_Ps*responsivity)
        variance_shotCurrentNoise = 2*1.6*(10**-19)*bandwidth*currentDueToSignalAndSBR_It
        variace_darkCurrentNoise = 2*1.6*(10**-19)*bandwidth*darkCurrent
        variance_thermalCurrentNoise = 4*1.38*(10**-23)*300*(bandwidth/loadResistance)
        SNR = CurrentDueToSignal_Ir/(np.sqrt(variace_darkCurrentNoise+variance_shotCurrentNoise+variance_thermalCurrentNoise))
        SNRdB = 20*np.log10(SNR)


        #updates the user interface labels with the calculated values
        self.ui.areaReceivingLens_AR.setText(str(areaReceivingLens_AR))
        self.ui.receiverBeamDiameter_Dl.setText(str(receiverBeamDiameter_Dl))
        self.ui.receiverBeamArea_AB.setText(str(receiverBeamArea_AB))
        self.ui.beamDivergenceLoss_Tbdl.setText(str(beamDivergenceLoss_Tbdl))
        self.ui.atmosphericExtinctionCoefficient_alpha.setText(str(atmosphericExtinctionCoefficient_alpha))
        self.ui.atmosphericTransmittance_Tatm.setText(str(atmosphericTransmittance_Tatm))
        self.ui.receivedPower_PR.setText(str(receivedPower_PR))
        self.ui.receivingLensFOV.setText(str(receivingLensFOV))
        self.ui.solidAngle.setText(str(solidAngle))
        self.ui.receivedsolarPower_Ps.setText(str(receivedsolarPower_Ps))
        self.ui.CurrentDueToSignal_Ir.setText(str(CurrentDueToSignal_Ir))
        self.ui.currentDueToSignalAndSBR_It.setText(str(currentDueToSignalAndSBR_It))
        self.ui.variance_shotCurrentNoise.setText(str(variance_shotCurrentNoise))
        self.ui.variace_darkCurrentNoise.setText(str(variace_darkCurrentNoise))
        self.ui.variance_thermalCurrentNoise.setText(str(variance_thermalCurrentNoise))
        self.ui.SNR.setText(str(SNR))
        self.ui.SNRdB.setText(str(SNRdB))

        calc()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())