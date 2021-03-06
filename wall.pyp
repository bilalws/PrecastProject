<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>PrecastProjectScripts\wall.py</Name>
        <Title>wall</Title>
        <Version>1.0</Version>
    </Script>
    <Page>
        <Name>Page1</Name>
        <Text>Wall</Text>

    <Parameter>
            <Name>Picture1</Name>
            <!-- referencing local image -->
            <Value>PictureForPalette.png</Value>
            <Orientation>Middle</Orientation>
            <ValueType>Picture</ValueType>
    </Parameter>

    <Parameter>
            <Name>Rowpic1</Name>
            <ValueType>Row</ValueType>
    <Parameter>
            <Name>Length1_1</Name>
            <Text>Wall Length</Text>
            <Value>4000</Value>
            <ValueType>Length</ValueType>
    </Parameter>
    <Parameter>
                <Name>ParamPicture1</Name>
                <!-- referencing local image -->
                <Value>param01.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
    </Parameter>

    <Parameter>
            <Name>Rowpic2</Name>            
            <ValueType>Row</ValueType>
    <Parameter>
            <Name>Width1_1</Name>
            <Text>Wall Height</Text>
            <Value>2500</Value>
            <ValueType>Length</ValueType>
    </Parameter>
    <Parameter>
                <Name>ParamPicture2</Name>
                <!-- referencing local image -->
                <Value>param02.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
    </Parameter>

    <Parameter>
            <Name>Rowpic3</Name>            
            <ValueType>Row</ValueType>

    <Parameter>
            <Name>Thickness1_1</Name>
            <Text>Wall Thickness</Text>
            <Value>100.0</Value>
            <ValueType>Length</ValueType>
    </Parameter>
	
	<Parameter>
                <Name>ParamPicture3</Name>
                <!-- referencing local image -->
                <Value>param03.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
    </Parameter>

    <Parameter>
            <Name>Expander</Name>
            <Text>Additional</Text>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>chkb_win</Name>
                <Text>Windows</Text>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>chkb_door</Name>
                <Text>Door</Text>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
            <Name>Rowpic4</Name>
            <ValueType>Row</ValueType>
            <Parameter>
                <Name>win_x</Name>
                <Text>Reference Widows from Wall Edge</Text>
                <Value>500.</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>ParamPicture4</Name>
                <!-- referencing local image -->
                <Value>param04.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
        	</Parameter>

        	<Parameter>
            <Name>Rowpic5</Name>
            <ValueType>Row</ValueType>
            <Parameter>
                <Name>win_z</Name>
                <Text>Reference Widows Height</Text>
                <Value>750.</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>ParamPicture5</Name>
                <!-- referencing local image -->
                <Value>param05.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
        	</Parameter>


        	<Parameter>
            <Name>Rowpic6</Name>
            <ValueType>Row</ValueType>
            <Parameter>
                <Name>win_length</Name>
                <Text>Window Width</Text>
                <Value>1000.</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>ParamPicture6</Name>
                <!-- referencing local image -->
                <Value>param06.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
        	</Parameter>

        	<Parameter>
            <Name>Rowpic7</Name>
            <ValueType>Row</ValueType>
            <Parameter>
                <Name>win_width</Name>
                <Text>Window Height</Text>
                <Value>1200.</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>ParamPicture7</Name>
                <!-- referencing local image -->
                <Value>param07.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
        	</Parameter>



            <Parameter>
                <Name>Separator1</Name>
                <ValueType>Separator</ValueType>
            </Parameter>


            <Parameter>
            <Name>Rowpic8</Name>
            <ValueType>Row</ValueType>
            <Parameter>
                <Name>door_x</Name>
                <Text>Reference Door from Wall Edge</Text>
                <Value>2200.</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>ParamPicture8</Name>
                <!-- referencing local image -->
                <Value>param08.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
        	</Parameter>

        	<Parameter>
            <Name>Rowpic9</Name>
            <ValueType>Row</ValueType>
            <Parameter>
                <Name>door_length</Name>
                <Text>Door Width</Text>
                <Value>1000.</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>ParamPicture9</Name>
                <!-- referencing local image -->
                <Value>param09.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
        	</Parameter>

        	<Parameter>
            <Name>Rowpic10</Name>
            <ValueType>Row</ValueType>
            <Parameter>
                <Name>door_width</Name>
                <Text>Door Height</Text>
                <Value>2000.</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>ParamPicture10</Name>
                <!-- referencing local image -->
                <Value>param10.png</Value>
                <ValueType>Picture</ValueType>
            </Parameter>
        	</Parameter>

    </Parameter>

    </Page>
    <Page>
        <Name>Page2</Name>
        <Text>Joins</Text>
    <Parameter>
            <Parameter>
            <Name>Expander</Name>
            <Text>Joins</Text>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>join1_type_active</Name>
                <Text>Adding Join1</Text>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
                <Name>join1_type</Name>
                <Text>Join1 Type</Text>
                <!-- selected value -->
                <Value>1</Value>
                <!-- list of possible values -->
                <ValueList>1|2|3</ValueList>
                <!-- list of picture file names -->
                <ValueList2>param01.png|param02.png|param03.png</ValueList2>
                <ValueType>PictureButtonList</ValueType>
                <Enable>join1_type_active == True</Enable>
            </Parameter>

            <Parameter>
                <Name>type1_a</Name>
                <Text>a</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <Enable>join1_type_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>type1_b</Name>
                <Text>b</Text>
                <Value>60</Value>
                <ValueType>Length</ValueType>
                <Enable>join1_type == 2</Enable>
            </Parameter>
            <Parameter>
                <Name>type1_c</Name>
                <Text>c</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <Enable>join1_type_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>type1_d</Name>
                <Text>d</Text>
                <Value>30</Value>
                <ValueType>Length</ValueType>
                <Enable>join1_type_active == True</Enable>
            </Parameter>

            <Parameter>
                <Name>join2_type_active</Name>
                <Text>Adding Join2</Text>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>

            <Parameter>
                <Name>join2_type</Name>
                <Text>Join2 Type</Text>
                <!-- selected value -->
                <Value>1</Value>
                <!-- list of possible values -->
                <ValueList>1|2|3</ValueList>
                <!-- list of picture file names -->
                <ValueList2>param01.png|param02.png|param03.png</ValueList2>
                <ValueType>PictureButtonList</ValueType>
                <Enable>join2_type_active == True</Enable>
            </Parameter>

            <Parameter>
                <Name>type2_a</Name>
                <Text>a</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <Enable>join2_type_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>type2_b</Name>
                <Text>b</Text>
                <Value>60</Value>
                <ValueType>Length</ValueType>
                <Enable>join2_type == 2</Enable>
            </Parameter>
            <Parameter>
                <Name>type2_c</Name>
                <Text>c</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <Enable>join2_type_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>type2_d</Name>
                <Text>d</Text>
                <Value>30</Value>
                <ValueType>Length</ValueType>
                <Enable>join2_type_active == True</Enable>
            </Parameter>
    </Parameter>
    </Parameter>

    </Page>

    <Page>
        <Name>Page3</Name>
        <Text>Shading</Text>
    <Parameter>
            <Parameter>
            <Name>Expander2</Name>
            <Text>Shading</Text>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>upper_shading_active</Name>
                <Text>Adding Upper Shading</Text>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>shading1_depth</Name>
                <Text>Shading Depth</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <Enable>upper_shading_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>shading1_b</Name>
                <Text>b</Text>
                <Value>60</Value>
                <ValueType>Length</ValueType>
                <Enable>upper_shading_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>shading1_thickness</Name>
                <Text>Shading Thickness</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <Enable>upper_shading_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>shading1_length</Name>
                <Text>Shading Length</Text>
                <Value>30</Value>
                <ValueType>Length</ValueType>
                <Enable>upper_shading_active == True</Enable>
            </Parameter>

            <Parameter>
                <Name>lower_shading_active</Name>
                <Text>Adding Lower Shading</Text>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>shading2_depth</Name>
                <Text>Shading Depth</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <Enable>lower_shading_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>shading2_b</Name>
                <Text>b</Text>
                <Value>60</Value>
                <ValueType>Length</ValueType>
                <Enable>lower_shading_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>shading2_thickness</Name>
                <Text>Shading Thickness</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <Enable>lower_shading_active == True</Enable>
            </Parameter>
            <Parameter>
                <Name>shading2_length</Name>
                <Text>Shading Length</Text>
                <Value>30</Value>
                <ValueType>Length</ValueType>
                <Enable>lower_shading_active == True</Enable>
            </Parameter>
    </Parameter>
    </Parameter>

    </Page>
</Element>
