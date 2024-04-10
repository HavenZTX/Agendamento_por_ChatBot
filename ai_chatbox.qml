import QtQuick 
import QtQuick.Controls.Material
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 500
    height: 400
    font.pixelSize: 20
    Material.theme: 'Dark'
    title: 'BORUS Chat'
    
    Rectangle{
        width: 400
        height: 300
        anchors.centerIn: parent 
    }
}