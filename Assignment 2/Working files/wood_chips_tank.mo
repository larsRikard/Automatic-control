model wood_chips_tank
  Modelica.Blocks.Continuous.Integrator h(y_start = 10)  annotation(
    Placement(visible = true, transformation(origin = {78, -92}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Division division annotation(
    Placement(visible = true, transformation(origin = {36, -90}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant rho(k = 145)  annotation(
    Placement(visible = true, transformation(origin = {-64, -70}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant A(k = 13.4)  annotation(
    Placement(visible = true, transformation(origin = {-64, -104}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant K_s(k = 0.5)  annotation(
    Placement(visible = true, transformation(origin = {-60, 38}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Product product annotation(
    Placement(visible = true, transformation(origin = {-10, -88}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Add add(k1 = -1)  annotation(
    Placement(visible = true, transformation(origin = {52, -10}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step w_out(height = 25)  annotation(
    Placement(visible = true, transformation(origin = {22, 42}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Product w_in annotation(
    Placement(visible = true, transformation(origin = {-2, -12}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Nonlinear.FixedDelay tau(delayTime = 250)  annotation(
    Placement(visible = true, transformation(origin = {-46, -22}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step u(height = 60, startTime = 1) annotation(
    Placement(visible = true, transformation(origin = {-96, -20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(division.y, h.u) annotation(
    Line(points = {{47, -90}, {54.5, -90}, {54.5, -92}, {66, -92}}, color = {0, 0, 127}));
  connect(rho.y, product.u1) annotation(
    Line(points = {{-53, -70}, {-23, -70}, {-23, -82}}, color = {0, 0, 127}));
  connect(A.y, product.u2) annotation(
    Line(points = {{-53, -104}, {-23, -104}, {-23, -94}}, color = {0, 0, 127}));
  connect(product.y, division.u2) annotation(
    Line(points = {{1, -88}, {13, -88}, {13, -96}, {24, -96}}, color = {0, 0, 127}));
  connect(add.y, division.u1) annotation(
    Line(points = {{63, -10}, {94.5, -10}, {94.5, -20}, {94, -20}, {94, -34}, {24, -34}, {24, -84}}, color = {0, 0, 127}));
  connect(w_out.y, add.u1) annotation(
    Line(points = {{33, 42}, {40, 42}, {40, -4}}, color = {0, 0, 127}));
  connect(K_s.y, w_in.u1) annotation(
    Line(points = {{-49, 38}, {-14, 38}, {-14, -6}}, color = {0, 0, 127}));
  connect(tau.y, w_in.u2) annotation(
    Line(points = {{-35, -22}, {-29.5, -22}, {-29.5, -18}, {-14, -18}}, color = {0, 0, 127}));
  connect(w_in.y, add.u2) annotation(
    Line(points = {{9, -12}, {39, -12}, {39, -16}}, color = {0, 0, 127}));
  connect(u.y, tau.u) annotation(
    Line(points = {{-85, -20}, {-74.5, -20}, {-74.5, -22}, {-58, -22}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "4.0.0")),
  Diagram(coordinateSystem(extent = {{-200, -200}, {200, 200}})),
  Icon(coordinateSystem(extent = {{-200, -200}, {200, 200}})),
  version = "");
end wood_chips_tank;
