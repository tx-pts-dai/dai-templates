# Discovery App Layer

This template is tailored on Discovery application deployment and it's meant to be applied after the (simple-app)[../../bases/simple-app] template.

Discovery applications rely on the same ALB while there's path base listener rule to forward the requests to the proper Target Group.

**Note**:

- the ALB is created in the discovery-infrastructure repository; a listener rule and target group dedicated to the service needs to be created before applying the simple-app and discovery-app templates
- the ALB for the preview branches (feature branches) is created by the annotations defined in the helm release terraform resource.
