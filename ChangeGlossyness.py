import bpy

def main():
    for mat in bpy.context.active_object.data.materials:
        if mat.use_nodes == True:
            nodes = mat.node_tree.nodes
            
            # get current glossy node:
            node_glossy = nodes.get("Glossy BSDF")
            glossyColor = node_glossy.inputs[0].default_value
            node_glossy.inputs[1].default_value = 0.3 # Roughness
            
            # get current hue/sat node:
            node_sat = nodes.get("Hue Saturation Value")
            node_sat.inputs[4].default_value = glossyColor
            node_sat.inputs[1].default_value = 1.15 # Saturation
            node_sat.inputs[2].default_value = 0.6 # Value

if __name__ == '__main__':
    main()