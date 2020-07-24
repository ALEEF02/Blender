import bpy

def main():
    for mat in bpy.context.active_object.data.materials:
        if mat.use_nodes == True:
            # If it's already using nodes, append a Hue Saturation Value node
            
            nodes = mat.node_tree.nodes
            
            # get current glossy node:
            node_glossy = nodes.get("Glossy BSDF")
            glossyColor = node_glossy.inputs[0].default_value
            node_glossy.inputs[1].default_value = 0.5 # Roughness
            
            # create hue/sat node
            node_sat = nodes.new(type='ShaderNodeHueSaturation')
            node_sat.inputs[4].default_value = glossyColor
            node_sat.inputs[1].default_value = 1.1 # Saturation
            node_sat.inputs[2].default_value = 1.0 # Value            
            node_sat.location = -150,300
            
            # link nodes
            links = mat.node_tree.links
            link = links.new(node_sat.outputs[0], node_glossy.inputs[0])
            
        if mat.use_nodes == False:
            ogColor = mat.diffuse_color
            
            # enable shading nodes
            mat.use_nodes = True
            nodes = mat.node_tree.nodes
            
            # delete default node
            nodes.clear()
            
            # create glossy node
            node_glossy = nodes.new(type='ShaderNodeBsdfGlossy')
            node_glossy.inputs[0].default_value = ogColor
            node_glossy.inputs[1].default_value = 8.0 # strength
            node_glossy.location = 0,0
            
            # create output node
            node_output = nodes.new(type='ShaderNodeOutputMaterial')   
            node_output.location = 400,0
            
            # link nodes
            links = mat.node_tree.links
            link = links.new(node_glossy.outputs[0], node_output.inputs[0])

if __name__ == '__main__':
    main()